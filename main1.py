from graphviz import Digraph

class TreeNode:
    def __init__(self, digit):
        self.digit = digit
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, digit):
        self.root = self._insert(self.root, digit)

    def _insert(self, node, digit):
        if node is None:
            return TreeNode(digit)
        if digit < node.digit:
            node.left = self._insert(node.left, digit)
        elif digit > node.digit:
            node.right = self._insert(node.right, digit)
        return node

    def search(self, digit):
        return self._search(self.root, digit)

    def _search(self, node, digit):
        if node is None or node.digit == digit:
            return node
        if digit < node.digit:
            return self._search(node.left, digit)
        else:
            return self._search(node.right, digit)

class HashMapTree:
    def __init__(self):
        self.hashmap = {}

    def insert_empty_tree(self, key):
        self.hashmap[key] = BinaryTree()

    def insert_digit(self, key, digit):
        if key in self.hashmap:
            self.hashmap[key].insert(digit)
        else:
            print(f"Tree not found for key {key}")

    def search_digit(self, key, digit):
        if key in self.hashmap:
            node = self.hashmap[key].search(digit)
            return node is not None
        else:
            print(f"Tree not found for key {key}")
            return False

    def visualize(self):
        dot = Digraph(comment='HashMapTree')

        for key, tree in self.hashmap.items():
            dot.node(key, key)
            self._visualize_tree(dot, tree.root, key)

        dot.render('hashmap_tree', format='png', cleanup=True)

    def _visualize_tree(self, dot, node, parent_key):
        if node:
            dot.node(f"{parent_key}_{node.digit}", str(node.digit))
            if node.left:
                dot.edge(f"{parent_key}_{node.digit}", f"{parent_key}_{node.left.digit}", label='L')
                self._visualize_tree(dot, node.left, parent_key)
            if node.right:
                dot.edge(f"{parent_key}_{node.digit}", f"{parent_key}_{node.right.digit}", label='R')
                self._visualize_tree(dot, node.right, parent_key)

# Example usage:
hashmap_tree = HashMapTree()

# Insert empty trees
hashmap_tree.insert_empty_tree("0")
hashmap_tree.insert_empty_tree("1")
hashmap_tree.insert_empty_tree("2")
hashmap_tree.insert_empty_tree("3")

# Insert digits into trees
hashmap_tree.insert_digit("0", 1)
hashmap_tree.insert_digit("0", 5)
hashmap_tree.insert_digit("0", 7)
hashmap_tree.insert_digit("0", 0)

# Visualize the hashmap
hashmap_tree.visualize()