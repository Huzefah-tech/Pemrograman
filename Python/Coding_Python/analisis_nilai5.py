import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Nilai': [80, 70, 90, 85, 75, 95, 80, 70, 85, 90],
    'Tinggi Badan': [165, 170, 175, 160, 180, 165, 170, 175, 160, 180]
}
df = pd.DataFrame(data)

# Histogram Nilai menggunakan Pandas
df['Nilai'].plot(kind='hist', bins=5, edgecolor='black', title="Distribusi Nilai")
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.show()

# Histogram Tinggi Badan menggunakan Pandas
df['Tinggi Badan'].plot(kind='hist', bins=5, edgecolor='black', title="Distribusi Tinggi Badan")
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.show()
