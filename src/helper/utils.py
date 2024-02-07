import collections
import hashlib
import random
import uuid
from typing import List
import linecache
from src.data_structure.hash_map_tree import HashMapTree
from src.db.db import db

def generate_short_uuid():
    # Generate a random UUID
    random_uuid = str(uuid.uuid4())

    # Use SHA-1 to hash the UUID, resulting in a 40 character hexadecimal string
    sha1_hash = hashlib.sha1(random_uuid.encode()).hexdigest()

    # Take the first 5 characters of the hash
    short_uuid = sha1_hash[:5]

    return short_uuid


def generate_seller_id(hashmap_tree: HashMapTree):
    key = "".join(generate_short_uuid())
    if not hashmap_tree.isKeyPresent(key):
        hashmap_tree.insert_empty_tree(key)
    else:
        generate_seller_id(hashmap_tree)


def check_if_key_exists(tree_string, key):
    list_of_strings = chunks(tree_string, 10)
    list_of_digits = [int(i) for i in str(key)]
    level = 0
    prev_next_count = 0
    reconstructed_length_array: List[List[int]] = [[] for _ in range(7)]
    reconstructed_fake_tree = [[] for _ in range(6)]
    for i in range(len(list_of_strings)):
        next_count = list_of_strings[i].count("1")
        reconstructed_length_array[level].append(next_count)
        reconstructed_fake_tree[level].append(list_of_strings[i])
        if i == 0 or len(reconstructed_length_array[level]) == prev_next_count:
            prev_next_count = sum(reconstructed_length_array[level], 0)
            level += 1
    kitne_avoid_krne_hai = [0 for _ in range(7)]
    
    onesBeforePosition = 0
    for level in range(len(reconstructed_fake_tree)):
        # for no_of_child in range(len(reconstructed_fake_tree[level])):
        isTrue, onesBeforePosition = isOneAtNPos(
            reconstructed_fake_tree[level][kitne_avoid_krne_hai[level]],
            list_of_digits[level],
        )
        kitne_avoid_krne_hai[level + 1] += onesBeforePosition + sum(reconstructed_length_array[level + 1][: kitne_avoid_krne_hai[level]], 0)
        if not isTrue:
            return False
    return True


def reconstruct_tree_from_string(tree_string, key):
    """
    Reconstructs a binary tree from a given string representation.

    Parameters:
    - tree_string (str): The string representation of the binary tree.
    - key (str): The key to identify the tree in the HashMapTree.

    Returns:
    - HashMapTree: The HashMapTree object containing the reconstructed binary tree.
    Note: This function assumes that the HashMapTree class and the BinaryTree class are already imported.
    """
    hashmap_tree = HashMapTree()
    hashmap_tree.insert_empty_tree(key)

    tree = hashmap_tree.hashmap[key]
    tree.insert_individual_digit(node=tree.root, digit=0)

    list_of_strings = chunks(tree_string, 10)

    reconstructed_length_array = [[] for _ in range(7)]
    reconstructed_fake_tree = [[] for _ in range(6)]

    level = 0
    prev_next_count = 0
    for i in range(len(list_of_strings)):
        next_count = list_of_strings[i].count("1")
        reconstructed_length_array[level].append(next_count)
        reconstructed_fake_tree[level].append(list_of_strings[i])
        if i == 0 or len(reconstructed_length_array[level]) == prev_next_count:
            prev_next_count = sum(reconstructed_length_array[level], 0)
            level += 1

    reconstructed_real_tree = [[] for _ in range(6)]
    for level in range(len(reconstructed_fake_tree)):
        for no_of_child in range(len(reconstructed_fake_tree[level])):
            new_array = []
            for index, bit in enumerate(reconstructed_fake_tree[level][no_of_child]):
                if bit == "1":
                    new_array.append(index)
            reconstructed_real_tree[level].append(new_array)

    queue = collections.deque()
    node = tree.root
    for level in reconstructed_real_tree:
        for child_indices in level:
            for index in child_indices:
                child = tree.insert_individual_digit(node, index)
                queue.append(child)
            node = queue.popleft()

    return hashmap_tree



"""
isse ye pta chalega ki kon sa child hai ye.
means ki next wale me itna avoid kr skte hai.
"""
def isOneAtNPos(string, position):
    if string[position] == "1":
        # 1's before the position
        onesBeforePosition = string[:position].count("1")
        return True, onesBeforePosition
    else:
        return False, -1


# def find_number_of_child_in_each_level_of


def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    return [s[i : i + n] for i in range(0, len(s), n)]


def insert_digit_wrapper(hashmap_tree, key, random_numbers):
    for number in random_numbers:
        hashmap_tree.insert_digit(key, number)


def generate_random_numbers(start, end, num):
    return [random.randint(start, end) for _ in range(num)]


def find_the_line_number_of_id(target_id):
    # with open(user_ids_file, 'r') as file:
        # user_ids = file.read().splitlines()

    low, high = 0, 10000 # in future it will be 10 million
    index = 0
    while low <= high:
        index += 1
        mid = (low + high) // 2
        current_id = ''.join(e for e in read_specific_line("id.txt", mid) if e.isalnum())
        # print(current_id, target_id)
        if current_id == target_id:
            # print(index)
            return mid
        elif current_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def read_specific_line(filename, line_number):
    return linecache.getline(filename, line_number)

def convert_data_to_string(data):
    ascii_8_length = chunks(data, 8)
    ascii_1_length = [bin_to_ascii(x) for x in ascii_8_length]
    # print(ascii_1_length)
    return "".join(ascii_1_length)

def bin_to_ascii(bin_str):
    # Convert binary string to integer
    int_val = int(bin_str, 2)
    
    # Convert integer to ASCII character
    ascii_char = chr(int_val)
    
    return ascii_char


def convert_string_to_data(ascii_str):
    # Convert ASCII characters to binary
    binary_str = ''.join(format(ord(ch), '08b') for ch in ascii_str)
    
    # Group binary string into chunks of 8 bits
    ascii_8_length = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    new_new_data = "".join(ascii_8_length[:-1])
    new_data_len_append = 10 - len(new_new_data)%10
    new_new_data += ascii_8_length[-1][-(new_data_len_append):]

    return new_new_data


def read_user_pins(line_number):
    found_value = db.get_value(line_number)
    print(f"value found at {line_number}:", found_value)
    found_data = convert_string_to_data(found_value)
    print('After converting value to binary:', found_data)  # print fetched binary value
    return found_data