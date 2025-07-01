# Import pustaka yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
# Membaca dataset dari file CSV
df = pd.read_csv("vehicles.csv")
# Menampilkan 5 data teratas
print(df.head())

# Pilih kolom-kolom yang akan digunakan untuk clustering
selected_columns = ['price', 'year', 'odometer', 'manufacturer', 'fuel', 'transmission', 'type', 'paint_color']
df = df[selected_columns]
# Hapus baris yang memiliki data kosong
df = df.dropna()
# Filter data: hanya ambil harga dan odometer yang masuk akal
df = df[(df['price'] > 1000) & (df['price'] < 100000)]
df = df[(df['odometer'] > 1000) & (df['odometer'] < 300000)]
# Tampilkan data yang sudah dibersihkan
print(df.describe())

# Tentukan fitur numerik dan kategorikal
numeric_features = ['price', 'year', 'odometer']
categorical_features = ['manufacturer', 'fuel', 'transmission', 'type', 'paint_color']
# Buat transformer untuk numerik dan kategorikal
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])
# Proses transformasi
X_preprocessed = preprocessor.fit_transform(df)
# Cek bentuk data hasil preprocessing
print(X_preprocessed.shape)

# Coba berbagai nilai k dari 1 sampai 10
inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_preprocessed)
    inertia.append(kmeans.inertia_)

# Visualisasi Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker='o')
plt.title('Elbow Method untuk Menentukan K')
plt.xlabel('Jumlah Cluster')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

# Jalankan KMeans dengan jumlah cluster optimal 
k_optimal = 3
kmeans = KMeans(n_clusters=k_optimal, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_preprocessed)

# Tambahkan hasil cluster ke dataframe asli
df['cluster'] = clusters

# Tampilkan ringkasan tiap cluster
print(df.groupby('cluster')[['price', 'year', 'odometer']].mean())

# Visualisasi hasil cluster dalam bentuk 2D dengan PCA
from sklearn.decomposition import PCA

# Reduksi ke 2 dimensi
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_preprocessed)

# Plot hasil clustering
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1], c=clusters, cmap='Set1', alpha=0.6)
plt.title('Visualisasi Cluster Mobil Craigslist (PCA 2D)')
plt.xlabel('PCA Komponen 1')
plt.ylabel('PCA Komponen 2')
plt.colorbar(scatter, label='Cluster')
plt.grid(True)
plt.show()
