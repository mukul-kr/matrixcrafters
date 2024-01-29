import hashlib
import random
import uuid

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
    key = ''.join(generate_short_uuid())
    if not hashmap_tree.isKeyPresent(key):
        hashmap_tree.insert_empty_tree(key)
    else:
        generate_seller_id(hashmap_tree)



def check_if_key_exists_helper(tree_string, element):
    pehle_kitne_hai = 0
    exist_krta_hai = False
    total_number_of_1s = 0
    for i in range(10):
        if tree_string[i] == str(1):
            if not exist_krta_hai:
                pehle_kitne_hai += 1
            total_number_of_1s += 1
        if i == element:
            exist_krta_hai = True
    if exist_krta_hai:
        return pehle_kitne_hai, total_number_of_1s
    else:
        return 0, 0


def check_if_key_exists(tree_string ,key):
    list_of_strings = chunks(tree_string, 10)
    list_of_digits = [int(i) for i in str(key)]

    pehle_kitne_hai = 0
    prev = 0
    total = 0
    purana_total_no_of_1s = 0
    total_no_of_1s = 0
    for i in range(6):
        print(f"index: {i} starting pehle_kitne_hai: {pehle_kitne_hai}, total_no_of_1s: {total_no_of_1s}, prev: {prev}, purana_total_no_of_1s: {purana_total_no_of_1s} string: {list_of_strings[prev]}")

        pehle_kitne_hai, total_no_of_1s = check_if_key_exists_helper(list_of_strings[prev], list_of_digits[i])
        prev += pehle_kitne_hai + purana_total_no_of_1s
        purana_total_no_of_1s = total_no_of_1s


        print(f"index: {i} ending pehle_kitne_hai: {pehle_kitne_hai}, total_no_of_1s: {total_no_of_1s}, prev: {prev}, purana_total_no_of_1s: {purana_total_no_of_1s} string: {list_of_strings[prev]}")


def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    return [s[i:i+n] for i in range(0, len(s), n)]



def insert_digit_wrapper(hashmap_tree, key, random_numbers):
    for number in random_numbers:
            hashmap_tree.insert_digit(key, number)


def generate_random_numbers(start, end, num):
    return [random.randint(start, end) for _ in range(num)]

