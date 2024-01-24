from graphviz import Digraph
import random
import string
import time
import threading

class TreeNode:
    def __init__(self, digit):
        self.digit = digit
        self.children = set()

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_digit_by_list(self, digit_list):
        self._insert(self.root, digit_list, 0)

    def _insert(self, node, digit_list, idx=0):
        if idx >= len(digit_list):
            return node
        if node is not None:
            for i in node.children:
                if i.digit == digit_list[idx]:
                    return self._insert(i, digit_list, idx + 1)
        # check if idx 0 is digit which is already present as value of root
        if idx == 0 and node is not None and node.digit == digit_list[idx]:
            return self._insert(node, digit_list, idx + 1)
        if node is None:
            newchild = TreeNode(digit_list[idx])
            self.root = newchild
        else:
            newchild = TreeNode(digit_list[idx])
            # node.children.append(newchild)
            node.children.add(newchild)
        return self._insert(newchild, digit_list, idx + 1)

    def search(self, digit_list):
        return self._search(self.root, digit_list)

    def _search(self, node, digit_list, idx=0):
        if idx >= len(digit_list) or node is None:
            return False
        if node.digit == digit_list[idx]:
            if idx == len(digit_list) - 1:
                return True
            for child in node.children:
                if self._search(child, digit_list, idx + 1):
                    return True
        return False

class HashMapTree:
    def __init__(self):
        self.hashmap = {}

    def insert_empty_tree(self, key):
        self.hashmap[key] = BinaryTree()



    def insert_digit(self, key, number):
        if key in self.hashmap:
            tree: BinaryTree = self.hashmap[key]
            list_of_digits = [int(digit) for digit in str(number)]
            tree.insert_digit_by_list(list_of_digits)
        else:
            print(f"Tree not found for key {key}")

    def search_digit(self, key, number):
        if key in self.hashmap:
            node = self.hashmap[key].search([int(digit) for digit in str(number)])
            return node is not None
        else:
            print(f"Tree not found for key {key}")
            return False



    def visualize_tree(self, key):
        # Check if key exists in the hashmap
        if key in self.hashmap:
            tree = self.hashmap[key]
            # Create a Graphviz object for visualization
            dot = Digraph(comment=key)
            # Generate DOT language script for the tree
            self._generate_dot_script(tree.root, dot, "")
            # Save and render the visualization
            filename = f"{key}_tree"
            dot.render(filename, format="png", cleanup=True)

    def _generate_dot_script(self, node, dot, parent_key):
        if node:
            dot.node(f"{parent_key}_{node.digit}", str(node.digit))
            for child in node.children:
                dot.edge(f"{parent_key}_{node.digit}", f"{parent_key}_{child.digit}", label='Child')
                self._visualize_tree(dot, child, parent_key)

    def visualize(self):
        dot = Digraph(comment='HashMapTree')

        for key, tree in self.hashmap.items():
            dot.node(key, key)
            self._visualize_tree(dot, tree.root, key)

        dot.render('hashmap_tree', format='png', cleanup=True)

    def _visualize_tree(self, dot, node, parent_key):
        if node:
            dot.node(f"{parent_key}_{node.digit}", str(node.digit))
            for child in node.children:
                dot.edge(f"{parent_key}_{node.digit}", f"{parent_key}_{child.digit}", label='Child')
                self._visualize_tree(dot, child, parent_key)

    def print_all_trees(self):
        for key, tree in self.hashmap.items():
            print(f"Key: {key}")
            print("Tree:")
            self._print_tree(tree.root, 0)
            print("\n")

    def _print_tree(self, node, depth):
        if node is not None:
            print(" " * depth + str(node.digit))
            for child in node.children:
                self._print_tree(child, depth + 1)


def insert_digit_wrapper(hashmap_tree, key, random_numbers):
    for number in random_numbers:
            hashmap_tree.insert_digit(key, number)


def generate_random_numbers(start, end, num):
    return [random.randint(start, end) for _ in range(num)]




# Example usage:

# Insert empty trees
# hashmap_tree.insert_empty_tree("0")
# hashmap_tree.insert_empty_tree("1")

# # Insert digits into trees
# hashmap_tree.insert_digit("0", 456789)
# hashmap_tree.insert_digit("0", 452749)
# hashmap_tree.insert_digit("0", 452741)
# hashmap_tree.insert_digit("0", 466789)
# hashmap_tree.insert_digit("1", 456789)
# hashmap_tree.insert_digit("1", 452789)


# hashmap_tree.print_all_trees()


# for i, j in hashmap_tree.hashmap.items():
#     print(j.search([int(digit) for digit in str(452749)]))
#     # hashmap_tree.visualize_tree(i)



# print()
        


if __name__ == "__main__":
    start_time = time.time()
    hashmap_tree = HashMapTree()

    for _ in range(1000):
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        hashmap_tree.insert_empty_tree(key)

    # For each key, generate between 1000-10000 random numbers and insert them into the corresponding tree
        
    # for key in hashmap_tree.hashmap.keys():
    #     num_elements = random.randint(1000, 10000)
    #     random_numbers = generate_random_numbers(100000, 999999, num_elements)
    #     for number in random_numbers:
    #         hashmap_tree.insert_digit(key, number)
    for key in hashmap_tree.hashmap.keys():
        num_elements = random.randint(100, 200)
        random_numbers = generate_random_numbers(100000, 999999, num_elements)
        # for number in random_numbers:
        t = threading.Thread(target=insert_digit_wrapper, args=(hashmap_tree, key, random_numbers))
        t.start()

    # hashmap_tree.visualize()

    # for i, j in hashmap_tree.hashmap.items():
    #     print(j.search([int(digit) for digit in str(452749)]))
        # hashmap_tree.visualize_tree(i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: {} seconds".format(elapsed_time))