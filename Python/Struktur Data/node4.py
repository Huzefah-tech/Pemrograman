# Definisi node untuk Linked List
class Node:
    def __init__(self, data):
        self.data = data        # Menyimpan data
        self.next = None        # Menyimpan referensi ke node berikutnya (pointer)

# Definisi kelas Linked List
class LinkedList:
    def __init__(self):
        self.head = None        # Head mengacu ke node pertama dalam Linked List

    # Teknik 1: Menambah elemen di akhir Linked List
    def append(self, data):
        new_node = Node(data)   # Buat node baru
        if self.head is None:   # Jika linked list kosong
            self.head = new_node
            return
        last = self.head
        while last.next:        # Cari node terakhir
            last = last.next
        last.next = new_node    # Tambahkan node baru di akhir

    # Teknik 2: Menambah elemen di awal Linked List
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Hubungkan node baru ke head saat ini
        self.head = new_node       # Update head menjadi node baru

    # Teknik 3: Menambah elemen setelah node tertentu
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Node sebelumnya harus ada dalam linked list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next  # Hubungkan node baru ke node setelah prev_node
        prev_node.next = new_node       # Hubungkan prev_node ke node baru

    # Teknik 4: Menghapus node berdasarkan data
    def delete_node(self, key):
        temp = self.head

        # Jika node yang akan dihapus adalah head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Cari node yang akan dihapus
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Jika data tidak ditemukan
        if temp is None:
            return

        # Hapus node dari linked list
        prev.next = temp.next
        temp = None

    # Teknik 5: Menampilkan seluruh elemen Linked List
    def display(self):
        current = self.head
        if current is None:
            print("Linked List kosong.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Contoh penggunaan Linked List
ll = LinkedList()

# Menambah elemen ke dalam Linked List
ll.append(10)
ll.append(20)
ll.append(30)
print("Linked List setelah menambah elemen di akhir:")
ll.display()

# Menambah elemen di awal Linked List
ll.insert_at_beginning(5)
print("Linked List setelah menambah elemen di awal:")
ll.display()

# Menambah elemen setelah node tertentu
ll.insert_after(ll.head.next, 15)
print("Linked List setelah menambah elemen setelah node kedua:")
ll.display()

# Menghapus elemen dari Linked List
ll.delete_node(20)
print("Linked list setelah menghapus elemen 20:")
ll.display()
