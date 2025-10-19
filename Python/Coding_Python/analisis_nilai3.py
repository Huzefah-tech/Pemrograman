import pandas as pd
import matplotlib.pyplot as plt

# Membuat DataFrame dengan data nilai dan tinggi badan
data = {'Nilai': [80, 70, 90, 85, 75, 95, 80, 70, 85, 90],
        'Tinggi Badan': [165, 170, 175, 160, 180, 165, 170, 175, 160, 180]}
df = pd.DataFrame(data)

# Menghitung statistik deskriptif dasar
mean_nilai = df['Nilai'].mean()
median_nilai = df['Nilai'].median()
modus_nilai = df['Nilai'].mode().values[0]

mean_tinggi_badan = df['Tinggi Badan'].mean()
median_tinggi_badan = df['Tinggi Badan'].median()
modus_tinggi_badan = df['Tinggi Badan'].mode().values[0]

# Menampilkan hasil statistik
print("Statistik Deskriptif:")
print(f"Mean Nilai: {mean_nilai}")
print(f"Median Nilai: {median_nilai}")
print(f"Modus Nilai: {modus_nilai}")

print(f"Mean Tinggi Badan: {mean_tinggi_badan}")
print(f"Median Tinggi Badan: {median_tinggi_badan}")
print(f"Modus Tinggi Badan: {modus_tinggi_badan}")

# Visualisasi data menggunakan Matplotlib
plt.figure(figsize=(10, 5))

# Histogram Nilai
plt.subplot(1, 2, 1)
plt.hist(df['Nilai'], bins=5, edgecolor='black', color='skyblue')
plt.title('Distribusi Nilai')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

# Histogram Tinggi Badan
plt.subplot(1, 2, 2)
plt.hist(df['Tinggi Badan'], bins=5, edgecolor='black', color='salmon')
plt.title('Distribusi Tinggi Badan')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Scatter Plot: Hubungan antara Nilai dan Tinggi Badan
plt.figure(figsize=(8, 6))
plt.scatter(df['Nilai'], df['Tinggi Badan'], color='purple')
plt.title('Hubungan antara Nilai dan Tinggi Badan')
plt.xlabel('Nilai')
plt.ylabel('Tinggi Badan (cm)')
plt.show()
