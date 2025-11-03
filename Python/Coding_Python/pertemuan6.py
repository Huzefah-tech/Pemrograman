#Tujuan:
# - Membuat DataFrame contoh (data nasabah / transaksi)
# - Melakukan analisis deskriptif sederhana
# - Membuat grafik otomatis (bar chart)
# - Menyimpan hasil ke fileExcel (.xlsx)
# - Menunjukkan cara download file Excel di Google Colab

# Langkah 1: 

import pandas as pd
import matplotlib.pyplot as plt
import os

# Langkah 2: Buat DataFrame contoh
# --------------------------------
# Data terstruktur contoh: data transaksi nasabah per cabang
data ={
  "ID_Nasabah": [101, 102, 103, 104, 105],
  "Nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
  "Saldo_Awal": [5000000, 35000000, 42000000, 60000000, 31000000],
  "Jenis_Kelamin": ["L", "L", "P", "P", "L"],
  "Transaksi_Bulan": [12000000, 8000000, 15000000, 20000000, 5000000],
  "Cabang": ["Jakarta", "Bandung", "Surabaya", "jakarta", "Bandung"]
  }
df = pd.DataFrame(data)

# Tampilkan DataFrame (di notebook ini akan muncul tabel)
print("Data Terstruktur (DataFrame):")
print(df)
