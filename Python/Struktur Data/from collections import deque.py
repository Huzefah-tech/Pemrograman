from collections import deque
dq = deque()

# Tambah dari belakang
dq.append("A")
dq.append("B")

# Tambah dari depan
dq.appendleft("C")
print("Isi Deque:", dq)

# Hapus dari belakang
print("Pop kanan:", dq.pop())

# Hapus dari depan
print("Pop kiri:", dq.popleft())
print("Isi Deque sekarang:", dq)