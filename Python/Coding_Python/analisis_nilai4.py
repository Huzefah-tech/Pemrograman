import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Nilai': [80, 70, 90, 85, 75, 95, 80, 70, 85, 90],
    'Tinggi Badan': [158, 170, 165, 159, 180, 160, 170, 175, 155, 167]
}
df = pd.DataFrame(data)

# Statistik deskriptif untuk Nilai
print("Statistik Deskriptif - Nilai")
print(f"Rata-rata (Mean): {df['Nilai'].mean()}")
print(f"Median: {df['Nilai'].median()}")
print(f"Modus: {df['Nilai'].mode().values[0]}")
print()

# Statistik deskriptif untuk Tinggi Badan
print("Statistik Deskriptif - Tinggi Badan")
print(f"Rata-rata (Mean): {df['Tinggi Badan'].mean()}")
print(f"Median: {df['Tinggi Badan'].median()}")
print(f"Modus: {df['Tinggi Badan'].mode().values[0]}")

# Visualisasi histogram
plt.figure(figsize=(10, 4))

# Histogram Nilai
plt.subplot(1, 2, 1)
plt.hist(df['Nilai'], bins=5, edgecolor='black')
plt.title("Distribusi Nilai")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")

# Histogram Tinggi Badan
plt.subplot(1, 2, 2)
plt.hist(df['Tinggi Badan'], bins=5, edgecolor='black')
plt.title("Distribusi Tinggi Badan")
plt.xlabel("Tinggi Badan (cm)")
plt.ylabel("Frekuensi")

plt.tight_layout()
plt.show()
