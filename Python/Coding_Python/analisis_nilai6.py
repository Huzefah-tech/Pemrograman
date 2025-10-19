import pandas as pd
import matplotlib.pyplot as plt

# Data 20 siswa
data = {
    'Nilai': [80, 70, 90, 85, 75, 95, 80, 70, 85, 90, 78, 82, 88, 76, 92, 84, 81, 79, 83, 77],
    'Tinggi Badan': [165, 170, 175, 160, 180, 165, 170, 175, 160, 180, 172, 168, 177, 162, 174, 169, 171, 166, 173, 167]
}
df = pd.DataFrame(data)

# Statistika deskriptif
print("Statistika Deskriptif:")
print(df.describe())

# Mean
print(f"\nMean Nilai: {df['Nilai'].mean()}")
print(f"Mean Tinggi Badan: {df['Tinggi Badan'].mean()}")

# Median
print(f"\nMedian Nilai: {df['Nilai'].median()}")
print(f"Median Tinggi Badan: {df['Tinggi Badan'].median()}")

# Modus
print(f"\nModus Nilai: {df['Nilai'].mode().values[0]}")
print(f"Modus Tinggi Badan: {df['Tinggi Badan'].mode().values[0]}")

# Histogram Nilai
df['Nilai'].plot(kind='hist', bins=5, edgecolor='black', title='Distribusi Nilai')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.show()

# Histogram Tinggi Badan
df['Tinggi Badan'].plot(kind='hist', bins=5, edgecolor='black', title='Distribusi Tinggi Badan')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.show()
