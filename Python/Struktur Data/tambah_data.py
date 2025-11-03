# Fungsi untuk menambah data mahsiswa
def tambah_data(mahasiswa, nama, nilai):
  mahasiswa[nama] = nilai

# Fungsi untuk menampilkan seluruh data mahasiswa
def tampilkan_data(mahasiswa):
  if mahasiswa:
    for nama, nilai in mahasiswa.items():
      print(f"Nama: {nama}, Nilai: {nilai}")
  else:
    print("Tidak ada data mahasiswa.")

# Fungsi untuk mencari nilai mahasiswa
def cari_nilai(mahasiswa, nama):
  return mahasiswa.get(nama, "Mahasiswa tidak ditemukan")

# Fungsi untuk memperbarui nilai mahasiswa
def update_nilai(mahasiswa, nama, nilai_baru):
  if nama in mahasiswa:
    mahasiswa[nama] = nilai_baru
    print(f"Nilai mahasiswa {nama} telah diperbarui.")
  else:
    print("Mahasiswa tidak ditemukan.")

# Main Program
mahasiswa = {}

while True:
  print("1. Tambah data mahasiswa")
  print("2. Tampilkan semua data mahasiswa")
  print("3. Cari nilai mahasiswa")
  print("4. Perbarui nilai mahasiswa")
  print("5. Keluar")
  pilihan = input("Pilih menu: ")
  if pilihan == '1':
    nama = input("Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai mahasiswa: "))
    tambah_data(mahasiswa, nama, nilai)
  elif pilihan == '2':
    tampilkan_data(mahasiswa)
  elif pilihan == '3':
    nama = input("Masukkan nama mahasiswa: ")
    print(cari_nilai(mahasiswa, nama))
  elif pilihan == '4':
    nama = input("Masukkan nama mahasiswa: ")
    nilai_baru = int(input("Masukkan nilai baru: "))
    update_nilai(mahasiswa, nama, nilai_baru)
  elif pilihan == '5':
    break
  else:
    print("Pilihan tidak valid.")