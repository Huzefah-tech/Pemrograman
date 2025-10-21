#Definisi Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None #pointer ke node berikutnya

#Definisi Linked List
class LinkedList:
  def __init__(self):
    self.head = None #head awalnya kosong
    #Tambah data di akhir (append)
  def append(self,data):
    new_node = Node(data)
    if self.head is None: #Jika linked list kosong
      self.head = new_node
      return
    last = self.head
    while last.next:      #iterasi ke node terakhir
      last = last.next
    last.next = new_node

#Cetak isi linked list
  def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

#Contoh penggunaan
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("Isi Linked List:")
ll.display()
