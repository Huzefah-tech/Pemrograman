# Fungsi untuk menambah data mahasiswa
def tambah_data(mahasiswa, nim, nama, nilai):
    mahasiswa[nim] = {"nama": nama, "nilai": nilai}

# Fungsi untuk menampilkan seluruh data mahasiswa
def tampilkan_data(mahasiswa):
    if mahasiswa:
        for nim, info in mahasiswa.items():
            print(f"NIM: {nim}, Nama: {info['nama']}, Nilai: {info['nilai']}")
    else:
        print("Tidak ada data mahasiswa.")

# Fungsi untuk mencari nilai mahasiswa berdasarkan NIM
def cari_nilai(mahasiswa, nim):
    if nim in mahasiswa:
        info = mahasiswa[nim]
        return f"Nama: {info['nama']}, Nilai: {info['nilai']}"
    else:
        return "Mahasiswa tidak ditemukan."

# Fungsi untuk memperbarui nilai mahasiswa
def update_nilai(mahasiswa, nim, nilai_baru):
    if nim in mahasiswa:
        mahasiswa[nim]["nilai"] = nilai_baru
        print(f"Nilai mahasiswa dengan NIM {nim} telah diperbarui.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Main Program
mahasiswa = {}

while True:
    print("\n=== Sistem Data Mahasiswa PT. Othinus ===")
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan semua data mahasiswa")
    print("3. Cari nilai mahasiswa")
    print("4. Perbarui nilai mahasiswa")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        nim = input("Masukkan NIM mahasiswa: ")
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        tambah_data(mahasiswa, nim, nama, nilai)

    elif pilihan == '2':
        tampilkan_data(mahasiswa)

    elif pilihan == '3':
        nim = input("Masukkan NIM mahasiswa: ")
        print(cari_nilai(mahasiswa, nim))

    elif pilihan == '4':
        nim = input("Masukkan NIM mahasiswa: ")
        nilai_baru = int(input("Masukkan nilai baru: "))
        update_nilai(mahasiswa, nim, nilai_baru)

    elif pilihan == '5':
        print("Terima kasih telah menggunakan sistem ini!")
        break

    else:
        print("Pilihan tidak valid.")
