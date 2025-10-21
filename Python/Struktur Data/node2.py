#Definisi Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None #pointer ke node berikutnya

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_head(self, data):
    new_node = Node(data)
    new_node.next = self.head #head lama jadi node berikutnya
    self.head = new_node      #update head

  def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

#Contoh penggunaan
ll = LinkedList()
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)
print("Isi Linked List (insert di head):")
ll.display()
