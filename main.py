import networkx as nx
from graphviz import Digraph

class HashMapWithTree:
    def __init__(self):
        self.hashmap = {}

    def insert_key(self, key):
        # Create an empty tree for the key
        tree = nx.DiGraph()
        self.hashmap[key] = tree

    def insert_digit(self, key, digit):
        # Check if key exists in the hashmap
        if key in self.hashmap:
            tree = self.hashmap[key]
            # Insert digit at the corresponding level in the tree
            tree.add_node(digit)

    def visualize_tree(self, key):
        # Check if key exists in the hashmap
        if key in self.hashmap:
            tree = self.hashmap[key]
            # Create a Graphviz object for visualization
            dot = Digraph(comment=key)

            # Add nodes to the Graphviz object
            for node in tree.nodes:
                dot.node(str(node))

            # Add edges to the Graphviz object
            for edge in tree.edges:
                dot.edge(str(edge[0]), str(edge[1]))

            # Save and render the visualization
            filename = f"{key}_tree"
            dot.render(filename, format="png", cleanup=True)

    def search_key(self, key):
        # Check if key exists in the hashmap
        return key in self.hashmap

# Example usage
hashmap_with_tree = HashMapWithTree()

# Insert keys with empty trees
hashmap_with_tree.insert_key("123456")
hashmap_with_tree.insert_key("654321")

# Insert digits into trees
hashmap_with_tree.insert_digit("123456", 1)
hashmap_with_tree.insert_digit("123456", 2)
hashmap_with_tree.insert_digit("123456", 3)

hashmap_with_tree.insert_digit("654321", 6)
hashmap_with_tree.insert_digit("654321", 5)
hashmap_with_tree.insert_digit("654321", 4)

# Visualize the trees
hashmap_with_tree.visualize_tree("123456")
hashmap_with_tree.visualize_tree("654321")

# Search for keys
print(hashmap_with_tree.search_key("123456"))  # Output: True
print(hashmap_with_tree.search_key("111111"))  # Output: False