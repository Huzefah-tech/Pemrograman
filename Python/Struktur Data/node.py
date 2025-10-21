# Definisi Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None #pointer ke node berikutnya

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def delete(self, key):
    temp = self.head

    # Jika node yang dihapus adalah head
    if temp and temp.data == key:
      self.head = temp.next
      temp = none
      return

    prev = None
    while temp and temp.data != key:
      prev = temp
      temp = temp.next
    if temp is None: # data tidak ditemukan
      return
    prev.next = temp.next
    temp = None
    
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
print("Sebelum hapus:")
ll.display()

ll.delete(20)
print("Sesudah hapus 20:")
ll.display()