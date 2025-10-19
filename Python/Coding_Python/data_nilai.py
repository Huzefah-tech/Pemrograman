import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV
data = pd.read_csv('file_io/data_nilaiDANtinggi_badan.csv')

# Tampilkan isi data
print("Data:")
print(data.to_string())

# Statistik untuk Nilai
mean_nilai = data['Nilai'].mean()
median_nilai = data['Nilai'].median()
modus_nilai = data['Nilai'].mode().values[0]

print("\n=== Statistik untuk Nilai ===")
print(f"Rata-rata (Mean): {mean_nilai}")
print(f"Median: {median_nilai}")
print(f"Modus: {modus_nilai}")

# Statistik untuk Tinggi Badan
mean_tinggi = data['Tinggi Badan'].mean()
median_tinggi = data['Tinggi Badan'].median()
modus_tinggi = data['Tinggi Badan'].mode().values[0]

print("\n=== Statistik untuk Tinggi Badan ===")
print(f"Rata-rata (Mean): {mean_tinggi}")
print(f"Median: {median_tinggi}")
print(f"Modus: {modus_tinggi}")

# Buat dua histogram berdampingan
plt.figure(figsize=(12, 5))

# Histogram Nilai
plt.subplot(2, 1, 1)  # baris 1, kolom 2, posisi 1
plt.hist(data["Nilai"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram Nilai")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")

# Histogram Tinggi Badan
plt.subplot(2, 1, 2)  # baris 1, kolom 2, posisi 2
plt.hist(data["Tinggi Badan"], bins=10, color='lightgreen', edgecolor='black')
plt.title("Histogram Tinggi Badan")
plt.xlabel("Tinggi Badan")
plt.ylabel("Frekuensi")

# Tampilkan kedua plot
plt.tight_layout()
plt.show()
