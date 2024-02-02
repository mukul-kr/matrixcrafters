import hashlib
import random
import uuid
from typing import List

from src.data_structure.hash_map_tree import HashMapTree


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
        kitne_avoid_krne_hai[level + 1] += onesBeforePosition + sum(
            reconstructed_length_array[level + 1][: kitne_avoid_krne_hai[level]], 0)
        if not isTrue:
            return False
    return True


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
    return [s[i: i + n] for i in range(0, len(s), n)]


def insert_digit_wrapper(hashmap_tree, key, random_numbers):
    for number in random_numbers:
        hashmap_tree.insert_digit(key, number)


def generate_random_numbers(start, end, num):
    return [random.randint(start, end) for _ in range(num)]


def find_the_line_number_of_id(target_id, user_ids_file):
    with open(user_ids_file, 'r') as file:
        user_ids = file.read().splitlines()

    low, high = 0, len(user_ids) - 1

    while low <= high:
        mid = (low + high) // 2
        current_id = user_ids[mid]

        if current_id == target_id:
            return mid + 1
        elif current_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return -1
