# Bubble short
def bubble_sort(arr):
  n= len(arr)
  for i in range(n-1):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j] #tukar posisi
  return arr

data = [34, 12, 56, 78, 23, 45]
print("Data sebelum dirutkan:", data)
print("Data setelah diurutkan (Bubble sort):", bubble_sort(data))