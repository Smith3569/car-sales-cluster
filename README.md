# 🚗 Craigslist Cars & Trucks Clustering

Proyek ini bertujuan untuk menganalisis dan mengelompokkan data mobil bekas yang diambil dari Craigslist menggunakan algoritma **K-Means Clustering**, serta memvisualisasikannya dalam bentuk 2D dengan **PCA**.

Dataset diambil dari: [Craigslist Cars and Trucks Dataset (by austinreese on Kaggle)](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)

---

## 📂 Struktur Proyek
The dataset used is vehicles.csv, which contains listings of thousands of used cars and trucks from Craigslist.

Key features used:
- **Price** – Harga kendaraan (USD).
- **Year** – Tahun kendaraan diproduksi.
- **Odometer** – Jarak tempuh (dalam mil/km).
- **Manufacturer**, **Fuel**, **Transmission**, **Type**, **Paint Color** – Fitur kategorikal yang dikonversi ke numerik.

---
## ⚙️ Data Preprocessing
Beberapa langkah preprocessing dilakukan:
- Menghapus data kosong (null/missing)
- Menghapus outlier pada kolom price dan odometer
- Standardisasi fitur numerik (StandardScaler)
- One-Hot Encoding untuk fitur kategorikal (OneHotEncoder)
- Gabungkan fitur menjadi matrix siap pakai untuk model ML

---

## 🧠 Modeling
Algoritma utama yang digunakan:
- **K-Means** Clustering dari scikit-learn
- Digunakan **Elbow** Method untuk menentukan jumlah cluster terbaik (k)
- Reduksi dimensi menggunakan **PCA (Principal Component Analysis)** untuk visualisasi 2D

---

## 📊 Hasil Clustering

Berikut adalah ringkasan rata-rata dari tiap cluster yang dihasilkan oleh algoritma K-Means:

| Cluster | Karakteristik Umum                  | Rata-rata Harga | Rata-rata Tahun | Rata-rata Odometer |
|---------|--------------------------------------|------------------|------------------|---------------------|
| 0       | Mobil murah dan lama                 | $8,500           | 2010             | 120,000 km          |
| 1       | Mobil menengah (standar)             | $14,000          | 2014             | 100,000 km          |
| 2       | Mobil baru, mahal, jarak tempuh rendah | $28,000         | 2018             | 60,000 km           |


