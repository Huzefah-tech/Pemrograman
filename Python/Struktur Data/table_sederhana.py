# Defenisi Table Sederhana
class HashTable:
    def __init__(self):
        self.table = [None] * 10  # Inisialisasi tabel dengan ukuran 10

    # Fungsi hash sederhana
    def hash_function(self, key):
        return key % 10

    # Menambah elemen ke hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    # Mengambil elemen dari hash table berdasarkan kunci
    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]

    # Menampilkan isi hash table
    def display(self):
        for index, value in enumerate(self.table):
            print(f"Index {index}: {value}")

# Contoh Penggunaan Hash Table
hash_table = HashTable()
hash_table.insert(10, "Data 1")
hash_table.insert(20, "Data 2")
hash_table.insert(30, "Data 3")

print("Isi Hash Table:")
hash_table.display()

print("Mencari data dengan kunci 20:", hash_table.search(20))