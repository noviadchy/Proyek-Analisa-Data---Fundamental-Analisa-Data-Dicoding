# Proyek Analisis Data: E-Commerce Public Dataset

Proyek akhir kelas **"Fundamental Analisa Data"** (Dicoding) menggunakan
Olist Brazilian E-Commerce Public Dataset.

- **Nama:** Novia Dwi Cahyanti
- **Email:** noviad079@gmail.com
- **ID Dicoding:** DS009B6X1394

## Struktur Direktori

```
submission
├───dashboard
│   ├───main_data.csv
│   └───dashboard.py
├───data
│   ├───customers_dataset.csv
│   ├───geolocation_dataset.csv
│   ├───order_items_dataset.csv
│   ├───order_payments_dataset.csv
│   ├───order_reviews_dataset.csv
│   ├───orders_dataset.csv
│   ├───product_category_name_translation.csv
│   ├───products_dataset.csv
│   └───sellers_dataset.csv
├───Proyek Analisis Data_Novia Dwi Cahyanti.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## Setup Environment

1. Buka **Command Prompt (CMD)**, lalu arahkan ke folder `submission` ini dengan perintah `cd`, contoh:
   ```
   cd "C:\Users\NamaUser\Desktop\submission"
   ```
2. (Opsional) Buat virtual environment agar library tidak bercampur dengan instalasi Python lain:
   ```
   python -m venv venv
   venv\Scripts\activate      # Mac/Linux: source venv/bin/activate
   ```
3. Install seluruh library yang dibutuhkan:
   ```
   pip install -r requirements.txt
   ```
   Tunggu sampai proses instalasi selesai (pandas, numpy, matplotlib, seaborn, streamlit).
4. Cek apakah Streamlit sudah terpasang dengan benar:
   ```
   streamlit --version
   ```
   Kalau muncul nomor versi (misalnya `Streamlit, version 1.63.0`), instalasi berhasil.

> **Catatan:** jika muncul error `WinError 32` atau `Connection timed out` saat `pip install`, biasanya disebabkan oleh sinkronisasi OneDrive/antivirus yang mengunci file sementara. Coba jalankan ulang perintah `pip install -r requirements.txt` sekali lagi (instalasi yang sudah selesai sebagian akan otomatis dilanjutkan).

## Menjalankan Notebook

Buka `Proyek Analisis Data_Novia Dwi Cahyanti.ipynb` dengan Jupyter Notebook/Jupyter Lab/Google Colab, lalu jalankan seluruh cell secara berurutan (Run All). Pastikan folder `data/` berada satu level dengan notebook tersebut.

```
jupyter notebook "Proyek Analisis Data_Novia Dwi Cahyanti.ipynb"
```

Menjalankan seluruh cell notebook ini (termasuk cell "Membuat main_data untuk dashboard" di bagian akhir, setelah Conclusion & Recommendation) akan otomatis menghasilkan ulang `dashboard/main_data.csv` yang menjadi sumber data dashboard Streamlit.

## Menjalankan Dashboard (Local)

Masih di jendela CMD yang sama (dari folder `submission`), jalankan:

```
cd dashboard
streamlit run dashboard.py
```

> **Catatan:** saat pertama kali menjalankan `streamlit run` akan muncul prompt untuk mengisi email (bersifat opsional dan tidak berkaitan dengan proses menjalankan dashboard). Boleh diisi apa saja atau dikosongkan, lalu tekan **Enter** dan dashboard akan otomatis terbuka di browser pada `http://localhost:8501`.

## Deploy ke Streamlit Cloud

Dashboard ini sudah di-deploy dan dapat diakses publik di:
**https://ecommerce-analysis-noviadchy.streamlit.app**

Langkah yang dilakukan untuk deploy:
1. Push file `dashboard.py`, `main_data.csv`, dan `requirements.txt` ke root repository GitHub.
2. Buka [share.streamlit.io](https://share.streamlit.io), login dengan akun GitHub, klik **New app**.
3. Klik **"Paste GitHub URL"**, lalu tempelkan URL langsung ke file `dashboard.py`, contoh:
   `https://github.com/noviadchy/Proyek-Analisa-Data---Fundamental-Analisa-Data-Dicoding/blob/main/dashboard.py`
   (Repository, branch, dan main file path otomatis terisi dari URL ini.)
4. Klik **Deploy** dan tunggu proses build selesai.
5. URL aplikasi yang dihasilkan dicatat di berkas `url.txt`.

## Sumber Data

Dataset: [E-Commerce Public Dataset (Olist Brazilian E-Commerce)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
