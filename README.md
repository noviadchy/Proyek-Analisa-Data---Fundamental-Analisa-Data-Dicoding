# Proyek Analisis Data: E-Commerce Public Dataset

Proyek akhir kelas **"Belajar Analisis Data dengan Python"** (Dicoding) menggunakan
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
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## Setup Environment

```
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Menjalankan Notebook

Buka `notebook.ipynb` dengan Jupyter Notebook/Jupyter Lab/Google Colab, lalu jalankan seluruh cell secara berurutan (Run All). Pastikan folder `data/` berada satu level dengan `notebook.ipynb`.

```
jupyter notebook notebook.ipynb
```

## Menjalankan Dashboard (Local)

```
cd dashboard
streamlit run dashboard.py
```

Dashboard akan otomatis terbuka di browser pada `http://localhost:8501`.

## Deploy ke Streamlit Cloud

1. Push seluruh folder `submission` (atau minimal folder `dashboard` beserta `main_data.csv`, dan `requirements.txt` di root repo) ke sebuah repository GitHub publik.
2. Buka [share.streamlit.io](https://share.streamlit.io), login dengan akun GitHub.
3. Klik **New app**, pilih repository, branch, dan set **Main file path** ke `dashboard/dashboard.py`.
4. Klik **Deploy**. Setelah proses build selesai, salin URL aplikasi yang diberikan.
5. Tempelkan URL tersebut ke berkas `url.txt`.

## Sumber Data

Dataset: [E-Commerce Public Dataset (Olist Brazilian E-Commerce)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
