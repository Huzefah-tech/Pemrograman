def selection_sort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_idx]:
          min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

#Main Program
penjualan = list(map(int, input("Masukkan data penjualan harian(maksimal 10 hari, pisahkan dengan spasi): ").split()))
selection_sort(penjualan)
print("Data penjualan setelah diurutkan:", penjualan)