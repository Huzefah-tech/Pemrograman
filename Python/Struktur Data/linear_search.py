# Linear Search

def linear_search(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i #Kembalikan posisi indeks
  return -1

data = [34, 12, 56, 78, 23, 45]
cari = 23
posisi = linear_search(data, cari)

if posisi != -1:
  print(f"Data {cari} ditemukan pada indeks ke-{posisi}")
else:
  print(f"Data {cari} tidak ditemukan")