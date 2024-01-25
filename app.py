
import random
import string
import time
import pickle
import threading
import datetime
import uuid
import logging
import json

import uuid
import hashlib

# logging.basicConfig(filename=f'info-{datetime.datetime.now()}.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig( encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TreeNode:
    def __init__(self, digit):
        self.digit = digit
        self.children = set()

    def to_dict(self):
        return {'d': self.digit, 'c': [child.to_dict() for child in self.children]}

class BinaryTree:
    def __init__(self):
        self.root = None

    def to_dict(self):
        return self.root.to_dict() if self.root else None

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
            logging.info(" " * depth + str(node.digit))
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





def generate_short_uuid():
    # Generate a random UUID
    random_uuid = str(uuid.uuid4())
    
    # Use SHA-1 to hash the UUID, resulting in a 40 character hexadecimal string
    sha1_hash = hashlib.sha1(random_uuid.encode()).hexdigest()
    
    # Take the first 5 characters of the hash
    short_uuid = sha1_hash[:5]
    
    return short_uuid


def generate_seller_id(hashmap_tree: HashMapTree):
    key = ''.join(generate_short_uuid())
    if not hashmap_tree.isKeyPresent(key):
        hashmap_tree.insert_empty_tree(key)
    else:
        generate_seller_id(hashmap_tree)

if __name__ == "__main__":
    start_time = time.time()
    hashmap_tree = HashMapTree()

    # hashmap_tree.insert_empty_tree("0")
    # hashmap_tree.insert_empty_tree("1")

    # # Insert digits into trees
    # hashmap_tree.insert_digit("0", 456789)
    # hashmap_tree.insert_digit("0", 452749)
    # hashmap_tree.insert_digit("0", 452741)
    # hashmap_tree.insert_digit("0", 466789)
    # hashmap_tree.insert_digit("1", 456789)
    # hashmap_tree.insert_digit("1", 452789)

    for _ in range(10):
        logging.info(_)
        generate_seller_id(hashmap_tree)


    # # hashmap_tree.print_all_trees()

    # # For each key, generate between 1000-10000 random numbers and insert them into the corresponding tree
        
    for key in hashmap_tree.hashmap.keys():
        num_elements = random.randint(1000, 10000)
        random_numbers = generate_random_numbers(100000, 999999, num_elements)
        for number in random_numbers:
            hashmap_tree.insert_digit(key, number)
    # # for key in hashmap_tree.hashmap.keys():
    # #     logging.info(f"inserting in {key}")
    # #     num_elements = random.randint(1000, 10000)
    # #     random_numbers = generate_random_numbers(100000, 999999, num_elements)
    # #     # for number in random_numbers:
    # #     t = threading.Thread(target=insert_digit_wrapper, args=(hashmap_tree, key, random_numbers))
    # #     t.start()
    

    out_file = open("myfile.json", "w")

    # Dump the Python object into the file
    json.dump(hashmap_tree.to_dict(), out_file)

    # Close the file
    out_file.close()

    end_time = time.time()
    # with open('my_file.pickle', 'wb') as file:
    # # Use pickle.dump() to save the object to the file
    #     pickle.dump(hashmap_tree, file)
    # elapsed_time = end_time - start_time

    
    

    # with open('my_file.pickle', 'rb') as file:
    # # Use pickle.dump() to save the object to the file
    #     hashmap_tree: HashMapTree = pickle.load(file)
    #     hashmap_tree.print_all_trees()
    #     print(f"answer {hashmap_tree.search_digit('0', 456789)}")


    # logging.info("Elapsed Time: {} seconds".format(elapsed_time))