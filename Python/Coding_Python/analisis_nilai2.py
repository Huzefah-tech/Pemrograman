import pandas as pd

# Buat dataframe dengan data nilai dan tinggi badan
data = {'Nilai': [80, 70, 90, 85, 75, 95, 80, 70, 85, 90],
        'Tinggi Badan': [165, 170, 175, 160, 180, 165, 170, 175, 160, 180]}
df = pd.DataFrame(data)

# Hitung statistik deskriptif (mean, median, modus)
mean_nilai = df['Nilai'].mean()
median_nilai = df['Nilai'].median()
modus_nilai = df['Nilai'].mode().values[0]

mean_tinggi_badan = df['Tinggi Badan'].mean()
median_tinggi_badan = df['Tinggi Badan'].median()
modus_tinggi_badan = df['Tinggi Badan'].mode().values[0]

# Menampilkan hasil statistik
print("Laporan Analisis Nilai dan Tinggi Badan\n")
print("1. Statistik Deskriptif\n")
print(f"  a. Nilai Siswa:")
print(f"    - Mean (Rata-rata) Nilai: {mean_nilai}")
print(f"    - Median (Nilai Tengah) Nilai: {median_nilai}")
print(f"    - Modus (Nilai yang Paling Sering Muncul) Nilai: {modus_nilai}\n")

print(f"  b. Tinggi Badan Siswa:")
print(f"    - Mean (Rata-rata) Tinggi Badan: {mean_tinggi_badan} cm")
print(f"    - Median (Tinggi Badan Tengah): {median_tinggi_badan} cm")
print(f"    - Modus (Tinggi Badan yang Paling Sering Muncul): {modus_tinggi_badan} cm\n")

# Menampilkan interpretasi
print("2. Interpretasi Data\n")
print(f"  - Nilai siswa memiliki rata-rata {mean_nilai}, dengan nilai tengah (median) {median_nilai}.")
print(f"    Nilai yang paling sering muncul adalah {modus_nilai}, menunjukkan bahwa sebagian besar siswa memiliki nilai sekitar {modus_nilai}.\n")
print(f"  - Tinggi badan siswa memiliki rata-rata {mean_tinggi_badan} cm, dengan nilai tengah (median) {median_tinggi_badan} cm.")
print(f"    Tinggi badan yang paling sering muncul adalah {modus_tinggi_badan} cm.\n")

# Menampilkan kesimpulan
print("3. Kesimpulan\n")
print(f"  - Rata-rata nilai siswa berada pada angka {mean_nilai}, yang menunjukkan kinerja siswa yang cukup baik.")
print(f"  - Sebagian besar siswa memiliki nilai sekitar {modus_nilai}, dengan distribusi nilai yang relatif merata.")
print(f"  - Rata-rata tinggi badan siswa adalah {mean_tinggi_badan} cm, dengan dua kelompok dominan yang memiliki tinggi badan {modus_tinggi_badan} cm.\n")
