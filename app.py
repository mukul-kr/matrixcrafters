
import time
import logging
from src.data_structure.hash_map_tree import HashMapTree
from src.db.db import CustomDatabase
from src.helper.utils import check_if_key_exists, convert_data_to_string, convert_string_to_data, find_the_line_number_of_id

logging.basicConfig(encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    hashmap_tree = HashMapTree()

    db = CustomDatabase("db.bin")

    user_id = 'bcd0d9'

    hashmap_tree.insert_empty_tree("0")

    hashmap_tree.insert_digit("0", 411111)
    hashmap_tree.insert_digit("0", 456789)
    hashmap_tree.insert_digit("0", 452749)
    hashmap_tree.insert_digit("0", 452741)
    hashmap_tree.insert_digit("0", 466789)
    hashmap_tree.insert_digit("0", 488888)
    hashmap_tree.insert_digit("0", 566789)

    # hashmap_tree.print_all_trees() # print the tree where data is stored

    for tree in hashmap_tree.hashmap.values():

        data = tree.create_data_to_save()

        data_to_save = convert_data_to_string(data)
        print('The data to save in db: ', data_to_save)
        '''
        # chunky is saved to db ? 

        # APIs In | routes | for:  
            ** create
            ** read
            ** update 
            ** delete
            ** search
            ** health_check
        '''
        line_number = find_the_line_number_of_id(user_id)
        if line_number != -1:
            print(f"User ID '{user_id}' found on line {line_number}.")
        else:
            print(f"User ID '{user_id}' not found in the file.")
        # here data_to_save is string '◄ @@►♦D ☻@►►♦☺☺'
        db.add_value_at_line(line_number, data_to_save)
        found_value = db.get_value(line_number)
        print(f"value found at {line_number}:", found_value)

        # compressed value to binary value
        found_data = convert_string_to_data(found_value)
        print('The fetched from dba nd converterd to original value',
              found_data)  # print fetched bianry value

        ''' don't know about this and why is it here? '''
        # chunky = ''.join(chunks(data, 8))
        # print(chunky, 'chunky')

        if data == found_data:
            print("\n data is same, from the time it was created and fetched from db.")
        else:
            print("Data is not same")

        print()
        isFound = check_if_key_exists(found_data, 456789)
        print(f"answer: {isFound}")
