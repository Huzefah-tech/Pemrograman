from collections import deque
# Membuat Queue
queue = deque()

# Menambah elemen ke Queue (Enqueue)
def enqueue(queue, item):
  queue.append(item)
  print(f"Elemen {item} telah ditambahkan ke queue.")

# Menghapus elemen dari Queue (Dequeue)
def dequeue(queue):
  if len(queue) == 0:
    print("Queue kosong. Tidak ada elemen yang dihapus.")
    return None
  removed_item = queue.popleft()
  print(f"Elemen {removed_item} telah dihapus dari queue")
  return removed_item

# Menampilkan elemen Queue
def display_dequeue(queue):
  print("Isi queue saat ini:", list(queue))

# Penggunaan Queue
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
display_dequeue(queue)
dequeue(queue)
display_dequeue(queue)