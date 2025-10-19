import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Baca data dari file CSV
df = pd.read_csv('data_nilai_tinggi.csv')

# Hitung statistika deskriptif
print("Statistika Deskriptif:")
print(df.describe())

# Hitung mean
mean_nilai = df['Nilai'].mean()
mean_tinggi_badan = df['Tinggi Badan'].mean()
print(f"\nMean Nilai: {mean_nilai}")
print(f"Mean Tinggi Badan: {mean_tinggi_badan}")

# Hitung median
median_nilai = df['Nilai'].median()
median_tinggi_badan = df['Tinggi Badan'].median()
print(f"\nMedian Nilai: {median_nilai}")
print(f"Median Tinggi Badan: {median_tinggi_badan}")

# Hitung modus
modus_nilai = df['Nilai'].mode().values[0]
modus_tinggi_badan = df['Tinggi Badan'].mode().values[0]
print(f"\nModus Nilai: {modus_nilai}")
print(f"Modus Tinggi Badan: {modus_tinggi_badan}")

# Hitung korelasi
korelasi = df['Nilai'].corr(df['Tinggi Badan'])
print(f"\nKorelasi antara Nilai dan Tinggi Badan: {korelasi}")

# Visualisasi data - Histogram
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df['Nilai'], bins=5, edgecolor='black')
plt.title('Distribusi Nilai')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
plt.hist(df['Tinggi Badan'], bins=5, edgecolor='black')
plt.title('Distribusi Tinggi Badan')
plt.xlabel('Tinggi Badan')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Visualisasi data - Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Nilai'], df['Tinggi Badan'])
plt.title('Hubungan antara Nilai dan Tinggi Badan')
plt.xlabel('Nilai')
plt.ylabel('Tinggi Badan')
plt.grid(True)
plt.show()