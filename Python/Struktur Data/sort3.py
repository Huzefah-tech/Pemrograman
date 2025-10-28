# Program 2: Mencari data penjualan tertentu menggunakan Linera Search
def linear_search(arr, target):
  for i in range(len(arr)):
      if arr[i] == target:
          return i
  return -1

#Main Program
penjualan = list(map(int, input("Masukkan data penjualan harian(pisahkan dengan spasi): ").split()))
target = int(input("Masukkan jumlah penjualan yang ingin dicari: "))
result = linear_search(penjualan, target)
if result != -1:
  print(f"Penjualan sebesar {target} ditemukan pada indeks ke-{result}")
else:
  print("Penjualan tidak ditemukan.")