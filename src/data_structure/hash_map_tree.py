import logging
from src.data_structure.binary_tree import BinaryTree

class HashMapTree:
    def __init__(self):
        self.hashmap = {}

    def to_dict(self):
        return {key: tree.to_dict() for key, tree in self.hashmap.items()}

    def insert_empty_tree(self, key):
        self.hashmap[key] = BinaryTree()

    def isKeyPresent(self, key):
        return key in self.hashmap


    def insert_digit(self, key, number):
        if key in self.hashmap:
            tree: BinaryTree = self.hashmap[key]
            list_of_digits = [int(digit) for digit in str(number)]
            tree.insert_digit_by_list(list_of_digits)
        else:
            logging.info(f"Tree not found for key {key}")

    def search_digit(self, key, number):
        if key in self.hashmap:
            node = self.hashmap[key].search([int(digit) for digit in str(number)])
            return node
        else:
            logging.info(f"Tree not found for key {key}")
            return False

    def _generate_dot_script(self, node, dot, parent_key):
        if node:
            dot.node(f"{parent_key}_{node.digit}", str(node.digit))
            for child in node.children:
                dot.edge(f"{parent_key}_{node.digit}", f"{parent_key}_{child.digit}", label='Child')
                self._visualize_tree(dot, child, parent_key)

    def _visualize_tree(self, dot, node, parent_key):
        if node:
            dot.node(f"{parent_key}_{node.digit}", str(node.digit))
            for child in node.children:
                dot.edge(f"{parent_key}_{node.digit}", f"{parent_key}_{child.digit}", label='Child')
                self._visualize_tree(dot, child, parent_key)

    def print_all_trees(self):
        for key, tree in self.hashmap.items():
            logging.info(f"Key: {key}")
            logging.info("Tree:")
            self._print_tree(tree.root, 0)
            logging.info("\n")

    def _print_tree(self, node, depth):
        if node is not None:
            logging.info("\t" * depth + str(node.digit))
            for child in node.children:
                self._print_tree(child, depth + 1)


hashmap_tree = HashMapTree()