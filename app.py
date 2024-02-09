
from fastapi.middleware.cors import CORSMiddleware
import logging
from src.data_structure.hash_map_tree import HashMapTree
from src.db.db import CustomDatabase
from src.helper.utils import check_if_key_exists, convert_data_to_string, convert_string_to_data, find_the_line_number_of_id
from fastapi import FastAPI
from src.routes import router as routes_router

logging.basicConfig(encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_router, prefix="/routes", tags=["routes"])

# import uvicorn

# uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

# if __name__ == "__main__":
#     hashmap_tree = HashMapTree()

#     db = CustomDatabase("base.db") ## renamed to .db file from .bin

#     user_id = 'bcd0d9'

#     # hashmap_tree.print_all_trees() # print the tree where data is stored

#     # for tree in hashmap_tree.hashmap.values():

#     #     data = tree.create_data_to_save()

#     #     data_to_save = convert_data_to_string(data)
        
#     #     line_number = find_the_line_number_of_id(user_id)
#     #     if line_number != -1:
#     #         print(f"User ID '{user_id}' found on line {line_number}.")
#     #     else:
#     #         print(f"User ID '{user_id}' not found in the file.")

#     #     # No use the file size is still 8KB even if sirectly insert string with serielization.
#     #     db.add_value_at_line(line_number, data_to_save)
#     #     found_value = db.get_value(line_number)
#     #     print(f"value found at {line_number}:", found_value)

#     #     # compressed value to binary value
#     #     found_data = convert_string_to_data(found_value)
#     #     print('The fetched from db and converterd to original value',
#     #           found_data)  # print fetched binary value

#     #     ''' don't know about this and why is it here? '''
#     #     # chunky = ''.join(chunks(data, 8))
#     #     # print(chunky, 'chunky')

#     #     if data == found_data:
#     #         print("\n data is same, from the time it was created and fetched from db.")
#     #     else:
#     #         print("Data is not same")

#     #     print()
#     #     isFound = check_if_key_exists(found_data, 456789)
#     #     print(f"answer: {isFound}")

    
