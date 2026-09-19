# Definisi Node untuk Binary Search Tree
class BSTNode:
    def __init__(self, key):
        self.key = key      # Nilai (key) dari node
        self.left = None    # Anak kiri
        self.right = None   # Anak kanan


# Definisi Binary Search Tree (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None    # Node root

    # Fungsi untuk menambah node baru ke BST
    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    # Fungsi pencarian node di BST
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # In-order traversal untuk BST
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.key, end=" ")
            self.in_order(node.right)

# Contoh penggunaan BST
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("\nBST In-order Traversal:")
bst.in_order(bst.root)

# Mencari node dalam BST
key_to_search = 60
result = bst.search(key_to_search)
if result:
    print(f"\nNode dengan key {key_to_search} ditemukan.")
else:
    print(f"\nNode dengan key {key_to_search} tidak ditemukan.")