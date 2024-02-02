
import time
import logging
from src.data_structure.hash_map_tree import HashMapTree
from src.helper.utils import check_if_key_exists, chunks, find_the_line_number_of_id
from src.db.db import CustomDatabase

logging.basicConfig(encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    start_time = time.time()
    hashmap_tree = HashMapTree()
    db = CustomDatabase("demo_db.bin")
    user_id = 'bcd0d9'
    data_value = '123'  # it may be string or number || update it to enter the data from tree
    line_number = find_the_line_number_of_id(user_id, "id.txt")
    if line_number != -1:
        print(f"User ID '{user_id}' found on line {line_number}.")
    else:
        print(f"User ID '{user_id}' not found in the file.")

    db.add_value_at_line(line_number, data_value)  # (line_number, data_value)
    print(f"value at {line_number}:", db.get_value(line_number))
    '''
    now, store :
    "only value without any key will be stored in.bin file" 
    "The data type will be either Integer or string"
    '''  # ✅

    # hashmap_tree.insert_empty_tree("0")
    # hashmap_tree.insert_empty_tree("1")

    # Insert digits into trees
    # hashmap_tree.insert_digit("0", 411111)
    # hashmap_tree.insert_digit("0", 456789)
    # hashmap_tree.insert_digit("0", 452749)
    # hashmap_tree.insert_digit("0", 452741)
    # hashmap_tree.insert_digit("0", 466789)
    # hashmap_tree.insert_digit("0", 488888)
    # hashmap_tree.insert_digit("0", 566789)
    # hashmap_tree.insert_digit("1", 456789)
    # hashmap_tree.insert_digit("1", 452789)

    # for _ in range(1):
    #     logging.info(_)
    #     generate_seller_id(hashmap_tree)

    # hashmap_tree.print_all_trees()

    # # For each key, generate between 1000-10000 random numbers and insert them into the corresponding tree

    # for key in hashmap_tree.hashmap.keys():
    #     num_elements = random.randint(100, 100)
    #     random_numbers = generate_random_numbers(100000, 999999, num_elements)
    #     for number in random_numbers:
    #         hashmap_tree.insert_digit(key, number)
    # # for key in hashmap_tree.hashmap.keys():
    # #     logging.info(f"inserting in {key}")
    # #     num_elements = random.randint(1000, 10000)
    # #     random_numbers = generate_random_numbers(100000, 999999, num_elements)
    # #     # for number in random_numbers:
    # #     t = threading.Thread(target=insert_digit_wrapper, args=(hashmap_tree, key, random_numbers))
    # #     t.start()

    for tree in hashmap_tree.hashmap.values():
        # tree.bfs()

        # data = tree.create_data_to_save()
        '''
        store, 'data'  ""data is a value"" data_value
        text file that will record  ✅
        line number from id.txt file and store valeu from data corresponding to the line number ✅

        use binary search for searching line numebr in the id.txt file ✅
        '''
        # for i in range(len(chunks(data, 10))):

        # print(f"({i} : {chunks(data, 10)[i]})", end=" ")
        # print()
        # print(f" store this data: {chunks(data, 8)}")
        # key_to_search = 456789
        # isFound = check_if_key_exists(data, key_to_search)
        # print(f"answer for query: {key_to_search}: {isFound}")

    # out_file = open("myfile.txt", "w")

    # # Dump the Python object into the file
    # # json.dump(hashmap_tree.to_dict(), out_file)

    # # Close the file
    # out_file.close()

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
