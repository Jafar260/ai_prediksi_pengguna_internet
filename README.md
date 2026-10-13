# 🌐 Prediksi Jumlah Pengguna Internet di Indonesia Berdasarkan Perkembangan Infrastruktur Digital

**By Kelompok [9]**

👥 **Anggota Kelompok:**
- [Audryl_Aulya_G.] ([F1G125054])
- [Awdiyah_Suhaila] ([F1G125004])
- [Jafar] ([F1G125034])

Proyek ini membangun model *supervised regression* untuk memprediksi jumlah pengguna internet di Indonesia berdasarkan perkembangan infrastruktur digital seperti jumlah BTS dan kapasitas Port Fiber Optic (FO). Model dilatih menggunakan data historis dan dievaluasi menggunakan beberapa algoritma machine learning untuk mendapatkan proyeksi yang akurat hingga tahun 2026.

## 📌 Latar Belakang

Transformasi digital di Indonesia berkembang sangat pesat seiring dengan masifnya pembangunan infrastruktur telekomunikasi, termasuk penambahan Base Transceiver Station (BTS) dan jaringan Fiber Optic. Namun, proyeksi pertumbuhan pengguna internet secara akurat sangat penting bagi pemerintah dan pelaku industri dalam perencanaan kebijakan serta ekspansi jaringan agar merata di seluruh wilayah.

Proyek ini mendukung **SDGS 9: Industri, Inovasi, dan Infrastruktur**. Model ini berfungsi sebagai alat bantu analitis berbasis data untuk mengukur dampak infrastruktur terhadap penetrasi internet di Indonesia.


## 📊 Dataset

- **Sumber:** Data Historis Infrastruktur & Pengguna Internet Indonesia (`BPS, APJII, KOMINFO`)
- **Jumlah Data:** [6] baris, [4] kolom
- **Fitur Terpilih (X):**
  - `Tahun`
  - `Jumlah BTS`
  - `Port FO (juta)`
- **Variabel Target (y):**
  - `Pengguna Internet (Juta)`


## 🛠️ Tools & Library

Proyek ini menggunakan beberapa tools dan library untuk mendukung proses pengolahan data, analisis korelasi, hingga pemodelan machine learning:

| Tools / Library | Kegunaan |
| :--- | :--- |
| **Python** | Bahasa pemrograman utama |
| **Google Colab / Jupyter** | Lingkungan pengembangan dan analisis dataset |
| **Pandas** | Membaca dan mengolah data tabular |
| **NumPy** | Operasi numerik dan manipulasi array |
| **Matplotlib & Seaborn** | Membuat visualisasi data dan heatmap korelasi |
| **Scikit-learn** | Training, pemodelan regresi, dan evaluasi model machine learning |
| **Tabulate** | Menampilkan tabel rapi di konsol/terminal |


## 📂 Struktur Repository

```text
.
├── Dataset Cleaning.xlsx
├── dataset_selected_features.csv
├── dataset_selected_features.xlsx
├── notebooks/
│   └── prediksi_pengguna_internet.ipynb
├── README.md
└── requirements.txt
```


## ⚙️ Metode

Proyek ini dilakukan melalui beberapa tahapan sistematis:

1. **Pengumpulan Data:** Menggunakan dataset sekunder terkait perkembangan infrastruktur digital dan jumlah pengguna internet di Indonesia.
2. **Preprocessing Data:** Pemeriksaan nilai kosong, pembersihan format, serta penyesuaian tipe data agar siap dianalisis.
3. **Analisis Korelasi:** Menghitung matriks korelasi antarvariabel untuk melihat hubungan linier dan mengidentifikasi faktor terkuat terhadap target.
4. **Feature Selection:** Memilih fitur utama yang memiliki kontribusi tertinggi terhadap prediksi pengguna internet (`Tahun`, `Jumlah BTS`, `Port FO (juta)`).
5. **Train-Test Split:** Membagi dataset menjadi data latih (80%) dan data uji (20%) dengan `random_state=42`.
6. **Pemodelan Machine Learning:** Melatih model regresi menggunakan algoritma *Linear Regression* dan *Random Forest Regressor*.
7. **Evaluasi Model:** Mengukur kinerja model menggunakan metrik evaluasi regresi ($R^2$ Score, MAE, dan RMSE).
8. **Prediksi & Interpretasi:** Melakukan proyeksi estimasi pengguna internet Indonesia untuk tahun 2026 serta menganalisis koefisien pengaruh fitur.


## 📈 Hasil & Evaluasi

| Algoritma | $R^2$ Score | MAE | RMSE |
| :--- | :--- | :--- | :--- |
| **Linear Regression** | **0.8472** | **0.9131** | 1.1532 |
| **Random Forest Regressor** | **-18.9299** | **12.835** | 13.1697 |

**Model Terbaik:** *Linear Regression* — dipilih sebagai model utama karena memiliki akurasi $R^2$ Score sebesar 84.72% dengan tingkat eror yang lebih stabil dibanding Random Forest pada dataset ini.

### Interpretasi & Proyeksi
- **Linear Regression** memberikan formula koefisien yang jelas untuk melihat pengaruh penambahan BTS dan port fiber optic terhadap peningkatan jumlah pengguna internet.
- **Prediksi Tahun 2026:** Berdasarkan skenario infrastruktur dengan $7.000$ BTS dan $14.0$ juta Port FO, diproyeksikan jumlah pengguna internet di Indonesia mencapai **[236.21] juta jiwa**.