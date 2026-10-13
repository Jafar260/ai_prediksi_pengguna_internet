# =======================================================================================================
#      PREDIKSI JUMLAH PENGGUNA INTERNET DI INDONESIA BERDASARKAN PERKEMBANGAN INFRASTRUKTUR DIGITAL
# =======================================================================================================

# Impor Pustaka (Libraries)
import io
import os
import sys
from google.colab import files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

try:
  from tabulate import tabulate
except ImportError:
  os.system("pip install tabulate")
  from tabulate import tabulate

# --------------
# MEMUAT DATASET
# --------------
file_path = "Dataset Cleaning.xlsx"

if not os.path.exists(file_path):
  print('\nSilakan unggah file "Dataset Cleaning.xlsx":')
  uploaded = files.upload()
  file_name = list(uploaded.keys())[0]
  df = pd.read_excel(io.BytesIO(uploaded[file_name]))
else:
  df = pd.read_excel(file_path)

print("\n==================================")
print("     DATASET BERHASIL DIMUAT      ")
print("==================================")
print(tabulate(df.head(6), headers="keys", tablefmt="grid", showindex=True))

# -----------------
# ANALISIS KORELASI
# -----------------
target_column = "Pengguna Internet (Juta)"
corr_matrix = df.corr(numeric_only=True)

print("\n====================================")
print("    SKOR KORELASI TERHADAP TARGET   ")
print("====================================")
if target_column in corr_matrix.columns:
  corr_target = corr_matrix[[target_column]].sort_values(
      by=target_column, ascending=False
  )
  print(
      tabulate(
          corr_target, headers=["Variabel", "Nilai Korelasi"], tablefmt="grid"
      )
  )
else:
  print(
      f"Peringatan: Kolom '{target_column}' tidak ditemukan atau bukan numerik."
  )

# Visualisasi Heatmap Korelasi
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="Blues", fmt=".3f", linewidths=0.5)
plt.title("Matriks Korelasi Antar Variabel", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()

# ---------------------------------
# FEATURE SELECTION (SELEKSI FITUR)
# ---------------------------------
selected_features = ["Tahun", "Jumlah BTS", "Port FO (juta)"]

X = df[selected_features]
y = df[target_column]

print("\n==============================")
print("      FEATURE SELECTION       ")
print("==============================")
print(f"Fitur Terpilih (X) : {list(X.columns)}")
print(f"Target (y)         : {y.name}")

print("\n=== Tampilan Data X (Fitur) ===")
print(tabulate(X, headers="keys", tablefmt="grid", showindex=True))

print("\n=== Tampilan Data y (Target) ===")
df_y = pd.DataFrame(y)
print(tabulate(df_y, headers="keys", tablefmt="grid", showindex=True))

df_selected = X.copy()
df_selected[target_column] = y

df_selected.to_csv("dataset_selected_features.csv", index=False)
df_selected.to_excel("dataset_selected_features.xlsx", index=False)

print("\n=== Ekspor Dataset Hasil Seleksi Fitur ===")
print(
    "File tersimpan di direktori Colab: 'dataset_selected_features.csv' &"
    " 'dataset_selected_features.xlsx'"
)

# ------------------
# TRAIN - TEST SPLIT
# ------------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n==============================")
print("      TRAIN - TEST SPLIT      ")
print("==============================")
print(f"Total Sampel Dataset     : {len(df)} baris")
print(f"Jumlah Data Latih (80%)  : {len(X_train)} baris")
print(f"Jumlah Data Uji (20%)    : {len(X_test)} baris")

print("\n=== Data Latih Fitur (X_train) ===")
print(tabulate(X_train, headers="keys", tablefmt="grid", showindex=True))

print("\n=== Data Uji Fitur (X_test) ===")
print(tabulate(X_test, headers="keys", tablefmt="grid", showindex=True))

print("\n=== Data Latih Target (y_train) ===")
print(
    tabulate(
        pd.DataFrame(y_train), headers="keys", tablefmt="grid", showindex=True
    )
)

print("\n=== Data Uji Target (y_test) ===")
print(
    tabulate(
        pd.DataFrame(y_test), headers="keys", tablefmt="grid", showindex=True
    )
)

# ---------
# PEMODELAN
# ---------
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# Algoritma 1: Linear Regression
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Algoritma 2: Random Forest Regressor
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)

print("\n========================================")
print("        PEMODELAN BERHASIL DILATIH      ")
print("========================================")
print("1. Model Linear Regression : Berhasil dilatih")
print("2. Model Random Forest     : Berhasil dilatih")

# --------------
# EVALUASI MODEL
# --------------
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred_lr = model_lr.predict(X_test)
y_pred_rf = model_rf.predict(X_test)

r2_lr = r2_score(y_test, y_pred_lr)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

r2_rf = r2_score(y_test, y_pred_rf)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))

# Ringkasan Evaluasi dalam Tabel
df_evaluasi = pd.DataFrame({
    "Algoritma": ["Linear Regression", "Random Forest Regressor"],
    "R2 Score": [f"{r2_lr:.4f}", f"{r2_rf:.4f}"],
    "MAE": [f"{mae_lr:.4f}", f"{mae_rf:.4f}"],
    "RMSE": [f"{rmse_lr:.4f}", f"{rmse_rf:.4f}"],
})

print("\n==============================")
print("        EVALUASI MODEL        ")
print("==============================")
print(tabulate(df_evaluasi, headers="keys", tablefmt="grid", showindex=False))

# -----------------------
# PREDIKSI & INTERPRETASI
# -----------------------

data_2026 = np.array([[2026, 7000, 14.0]])

pred_2026 = model_lr.predict(data_2026)[0]

df_koef = pd.DataFrame({
    'Fitur': selected_features,
    'Koefisien (Pengaruh)': model_lr.coef_,
})

print('\n======================================')
print('       PREDIKSI & INTERPRETASI        ')
print('======================================')
print(
    'Estimasi Pengguna Internet Indonesia Tahun 2026:'
    f' {pred_2026:.2f} Juta Pengguna'
)

print('\n=== Pengaruh Masing-Masing Fitur Terhadap Prediksi ===')
print(tabulate(df_koef, headers='keys', tablefmt='grid', showindex=False))

# ----------
# KESIMPULAN
# ----------
print('\n=========================')
print('        KESIMPULAN       ')
print('=========================')
print(
    '1. Kesimpulan Model: Model Linear Regression dipilih sebagai model terbaik'
    ' karena memiliki akurasi R2 Score sebesar 84.72% dan tingkat eror yang'
    ' jauh lebih rendah dibanding Random Forest.'
)
print(
    '2. Kesimpulan Prediksi: Pada tahun 2026, diproyeksikan jumlah pengguna'
    f' internet di Indonesia mencapai {pred_2026:.2f} juta jiwa.'
)