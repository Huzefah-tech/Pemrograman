from collections import deque
# Membuat Dequeue
dequeue = deque()

# Menambah elemen ke Dequeue di belakang (Append)
def enqueue_back(dequeu, item):
  dequeue.append(item)
  print(f"Elemen {item} telah ditambahkan ke belakang dequeue.")

# Menambah elemen ke Dequeue di depan (Appendleft)
def enqueue_front(dequeu, item):
  dequeue.append(item)
  print(f"Elemen {item} telah ditambahkan ke depan dequeu.")

# Menghapus elemen dari belakang Dequeue (Pop)
def dequeue_back(dequeue):
  if len(dequeue) == 0:
    print("Dequeue kosong. Tidak ada elemen yang dihapus.")
    return None
  removed_item = dequeue.pop()
  print(f"Elemen {removed_item} telah dihapus dari belakang dequeue.")
  return removed_item

# Menghapus elemen dari depan Dequeue (Popleft)
def dequeue_front(dequeue):
  if len(dequeue) == 0:
    print("Dequeue kosong. Tidak ada elemen yang dihapus.")
    return None
  removed_item = dequeue.pop()
  print(f"Elemen {removed_item} telah dihapus dari belakang dequeue.")
  return removed_item

# Menampilkan elemen Dequeue
def display_dequeue(dequeue):
  print("Isi dequeue saat ini:", list(dequeue))

# Penggunaan Dequeue
enqueue_back(dequeue, 10)
enqueue_back(dequeue, 20)
enqueue_front(dequeue, 5)
display_dequeue(dequeue)

dequeue_front(dequeue)
display_dequeue(dequeue)

dequeue_back(dequeue)
display_dequeue(dequeue)