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

🧠 Modeling
Algoritma utama yang digunakan:
- **K-Means**- Clustering dari scikit-learn
- Digunakan - **Elbow** Method untuk menentukan jumlah cluster terbaik (k)
- Reduksi - dimensi menggunakan **PCA (Principal Component Analysis)** untuk visualisasi 2D

