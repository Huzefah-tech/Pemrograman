# Konverter Mata Uang Sederhana
print("=== Konverter Mata Uang ===")

# Nilai tukar tetap (contoh saja)
kurs = {
  "USD": 15000, # 1 USD = 15.000 IDR
  "JPY": 100,   # 1 JPY = 100 IDR
  "EUR": 16500, # 1 EUR = 16.500 IDR
}

print("Mata uang tersedia: USD, JPY, EUR")

asal = input("Masukkan mata uang asal (contoh: USD): ").upper()
jumlah = float(input("Masukkan jumlah uang: "))
tujuan = input("Masukkan mata uang tujuan (contoh: IDR): ").upper()

# Konversi ke IDR terlebih dahulu
if asal != "IDR":
  jumlah_idr = jumlah * kurs.get(asal, 1)
else:
  jumlah_idr = jumlah

# Konversi dari IDR ke mata uang tujuan
if tujuan != "IDR":
    hasil = jumlah_idr / kurs.get(tujuan, 1)
else:
    hasil = jumlah_idr

print(f"\n{jumlah} {asal} = {hasil:.2f} {tujuan}")