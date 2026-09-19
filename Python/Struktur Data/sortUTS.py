# ============================================
# Program: Data Penjualan PT. Othinus
# Fitur: Mengurutkan & Mencari Data Penjualan
# ============================================

# Fungsi untuk mengurutkan data penjualan (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Tukar posisi
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Fungsi untuk mencari data penjualan (Linear Search)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# ==========================
# Main Program
# ==========================

print("=== Program Data Penjualan PT. Othinus ===")

# Input data penjualan
penjualan = list(map(int, input("Masukkan data penjualan harian (maksimal 10 hari, pisahkan dengan spasi): ").split()))

# Urutkan data penjualan
selection_sort(penjualan)
print("\nData penjualan setelah diurutkan (terkecil → terbesar):")
print(penjualan)

# Tampilkan penjualan tertinggi dan terendah
print(f"Penjualan terendah: {penjualan[0]}")
print(f"Penjualan tertinggi: {penjualan[-1]}")

# Pencarian data penjualan tertentu
target = int(input("\nMasukkan jumlah penjualan yang ingin dicari: "))
result = linear_search(penjualan, target)

if result != -1:
    print(f"Penjualan sebesar {target} ditemukan pada indeks ke-{result}")
else:
    print("Penjualan tidak ditemukan.")

print("\n=== Program Selesai ===")
