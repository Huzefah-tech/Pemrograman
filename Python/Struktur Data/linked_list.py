# ==========================================
# Implementasi Lengkap Linked List di Python
# ==========================================

# Definisi Node
class Node:
  def __init__(self, data):
    self.data = data        # Menyimpan data node
    self.next = None        # Menunjuk ke node berikutnya (pointer)

# Definisi Linked List 
class LinkedList:
  def __init__(self):
    self.head = None        # Head mengacu pada node pertama

  # Tambah node di akhir
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  # 2️⃣ Tambah node di awal
  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  # 3 Tambah node setelah node tertentu
  def insert_after(self, prev_node, data):
    if prev_node is None:
      print("Node sebelumnya tidak boleh None.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  # 4 Hapus node berdasarkan data
  def delete_node(self, key):
    temp = self.head

    # Jika node pertama (head) yang dihapus
    if temp is not None:
      if temp.data == key:
        self.head = temp.next
        temp = None
        return

    prev = None 
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next

    if temp is None: #Jika data tidak ditemukan
      print(f"Data {key} tidak ditemukan dalam Linked List.")
      return

    prev.next = temp.next
    temp = None

  # 5 Tampilkan isi Linked List
  def display(self):
    current = self.head
    if current is None:
      print("Linked List kosong.")
      return
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")


# =============================
# Contoh penggunaan Linked List
# =============================

ll = LinkedList()

# Tambah data di awal
ll.insert_at_beginning(5)
print("Setelah insert data awal:")
ll.display()


# Tambah data di akhir
ll.append(10)
ll.append(20)
ll.append(30)
print("setelah append (tambah di akhir):")
ll.display()

# Tabah data setelah node kedua
ll.insert_after(ll.head.next, 15)
print("setelah node kedua:")
ll.display()

# Hapus data tertentu
ll.delete_node(10)
print("setelah menghapus node:")
ll.display()

ll.insert_after(ll.head.next, 17)
ll.display()