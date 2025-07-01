# 🚗 Craigslist Cars & Trucks Clustering

Proyek ini bertujuan untuk menganalisis dan mengelompokkan data mobil bekas yang diambil dari Craigslist menggunakan algoritma **K-Means Clustering**, serta memvisualisasikannya dalam bentuk 2D dengan **PCA**.

Dataset diambil dari: [Craigslist Cars and Trucks Dataset (by austinreese on Kaggle)](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data)

---

## 📂 Struktur Proyek

craigslist-clustering/
├── data/
│   └── vehicles.csv               # Dataset asli dari Kaggle
│
├── notebooks/
│   └── craigslist_clustering.ipynb # Jupyter Notebook (opsional)
│
├── src/
│   └── preprocessing.py           # Fungsi preprocessing data
│   └── clustering.py              # Proses KMeans, PCA, Elbow
│   └── visualization.py           # Fungsi plotting
│
├── outputs/
│   ├── clustered_vehicles.csv     # Output data dengan label cluster
│   ├── elbow_plot.png             # Gambar elbow method
│   └── cluster_2d_pca.png         # Visualisasi hasil clustering 2D
│
├── README.md                      # Dokumentasi proyek
├── requirements.txt               # Daftar pustaka yang dibutuhkan
└── main.py                        # Main script jika ingin satu file run semua
