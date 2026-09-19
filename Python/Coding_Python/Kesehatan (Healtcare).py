# Kesehatan (Healthcare)

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# -----------------------------------
# 1. Simulasi Data Big Data Kesehatan
# -----------------------------------

np.random.seed(42)

n = 500 # Jumlah pasien

# Rekam medis elektronik (EMR)
emr = pd.DataFrame({
  "usia": np.random.randint(20, 80, n),
  "jenis kelamin": np.random.choice([0, 1], n), # 0: perempuan, 1: laki-laki
  "riwayat_diabetes": np.random.choice([0, 1], n),
  "riwayat_hipertensi": np.random.choice([0, 1], n),
})

# Hasil laboratorium
lab = pd.DataFrame({
  "kolesterol": np.random.randint(150, 300, n),
  "gula_darah": np.random.randint(70, 250, n),
})

# Data wearable (smartwatch, sensor)
wearable = pd.DataFrame({
  "detak_jantung_rata2": np.random.randint(60, 140, n),
  "langkah_per_hari": np.random.randint(1000, 12000, n),
})

# Cintra medis (MRI/CT) disimulasikan sebagai skor numerik
medical_image = pd.DataFrame({
  "citra_skor_anomali": np.random.rand(n) * 10
})

# Label risiko penyakit jantung (target)
# dibuat berdasarkan kombinasi fitur (bukan data medis nyata)
risk = (
  (emr["usia"] > 50).astype(int)
  + (lab["kolesterol"] > 240).astype(int)
  + (lab["gula_dara"] > 180).astype(int)
  + (wearable["detak_jantung_rata2"] > 110).astype(int)
  + (medical_image["citra_skor_anomali"] > 7).astype(int)
)

target = (risk >= 2).astype(int) # 1 = risiko tinggi

# ==============================================
# 2. Gabimglam semua data -> big data healthcare
# =============================================

data = pd.concat([emr, lab, wearable, medical_image], axis=1)
data["resiko_jantung"] = target

print("Contoh data:")
print(data.head())

# ============================
# 3. training machine learning
# ============================

X = data.drop("resiko_jantung", axis=1)
y = data["resiko_jantung"] = target

X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.25, random_state=0
)

model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nHasil evaluasi model:")
print(classification_report(y_test, y_pred))

# ==============================
# 4. contoh prediksi pasien baru
# ==============================

pasien_baru = pd.DataFrame({
  "usia": [55],
  "jenis_kelamin": [1],
  "riwayat_diabetes": [1],
  "riwayat_hipertensi": [1],
  "kolesterol": [260],
  "gula_darah": [200],
  "detak_jantung_rata2": [120],
  "langkah_per_hari": [3000],
  "citra_skor_anomali": [8.2]
})

prediksi = model.predict(pasien_baru)[0]
prob = model.predict_proba(pasien_)baru[0][1]

print("\nPrediksi risiko pasien baru:")
print("Probabilitas risiko jantung:", round(prob, 3))
print("Kategori:", "TINGGI" if prediksi == 1 else "RENDSH")

# ===================================
# 5. REKOMENDASI PERAWATAN PRESONAL SEDERHANA
# ===================================

rekomendasi_perawatan(prob_risk):
if prob_risk > 0.8:
  return "Perlu rujukan spesialis jantung + pemeriksaan lengkap"
elif prob_risk > 0.6:
  return "Pantau ketat, terapi gaya hidup + konsultasi rutin"
elif prob_risk > 0.3:
  return "Perbaiki pola makan & olahraga"
else:
  return "Risiko rendah, tetap jaga kesehatan"

print("Rekomendasi:", rekomendasi_perawatan(prob))

# ========================
# 6. ANALISIS STOK OBAT (FORECAST SEDERHANA)
# ========================

# Simulasi kebutuhan obat untuk hipertensi
jumlah_pasien_bulan = np.random.randint(200, 400, 12)

stok_awal = 500
pemakaian = jumlah_pasien_bulan * 2 # 2 tablet per pasien

sisa_stok = stok_awal - pemakaian.cumsum()

print("\nSimulasi sisa stok obat per bulan:")
print(sisa_stok)

if any(sisa_stok < 0):
  print("PERINGATAN: stok obat diprediksi habis - perlu pengadaan ulang")
else:
  print("stok obat aman")