class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    # Fungsi rekursif untuk menyisipkan node sesuai aturan BST
    def _insert_recursively(node, data):
      if node is None:
        return Node(data)
      if data < node.data: #Masuk subree kiri jika lebih kecil
        node.left = _insert_recursively(node.left, data)
      else: # Masuk subtree kanan jika lebih besar atau sama
        node.right = _insert_recursively(node.right, data)
      return node

    if self.root is None:
      self.root = Node(data)
    else:
      _insert_recursively(self.root, data)

  def display_tree(self):
    if not self.root:
      print("Tree is empty")
      return
    
    # Menggunakan traversal level-order untuk menyimpan node per level
    queue = [(self.root, 0)] # Simpan node beserta levelnya
    levels = {}

    while queue:
      node, level = queue.pop(0)
      if level not in levels:
        levels[level] = []
      levels[level].append(node.data if node else None)
      if node:
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))

    # Cetak pohon secara hierarkis
    max_level = max(level.keys())
    max_width = 2 ** max_level # Lebar maksimum untuk simetri
    for level in range(max_level + 1):
      spacing = max_width // (2 ** level)
      line = ""
      for value in levels[level]:
        if value is None:
          line += " " * (spacing * 2)
        else:
          line += f"{value:^{spacing * 2}}"
    print(line.rstrip())

# Membuat Binary Search Tree
bst = BinarySearchTree()

# Menambahkan data ke dalam BST
values = [40, 20, 60, 10, 30, 50, 80, 5, 15, 25, 35, 55, 70,90,
          3, 13, 27, 65, 75, 85, 95, 1, 12, 14, 61, 72, 87]

for value in values:
  bst.insert(value)

# Menampilkan pohon
bst.display_tree()
