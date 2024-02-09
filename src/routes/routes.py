
from fastapi import APIRouter, Query
from src.data_structure.binary_tree import BinaryTree
from src.data_structure.hash_map_tree import HashMapTree
# from src.data_structure.hash_map_tree import hashmap_tree
from src.db.db import db

from src.helper.utils import check_if_key_exists, convert_data_to_string, convert_string_to_data, find_the_line_number_of_id, read_specific_line, read_user_pins, reconstruct_tree_from_string
from src.routes.schema import UserPinData

router = APIRouter()

@router.get("/health_check")
def health_check():
    return {"status": "OK"}

@router.get("/read")
def read(seller_id: str = Query(..., alias="seller_id"), pin: str = Query(...)):
    read_line = find_the_line_number_of_id(seller_id)
    print('line_number:', read_line)
    if read_line == -1:
        return {"message": f"{seller_id} doesn't exist in our database"}
    
    fetch_user_pins = read_user_pins(read_line)
    print('fetch_user_pins:', fetch_user_pins)
    user_pins = [pin for pin in fetch_user_pins]
    if pin not in user_pins:
        return {"message": f"{pin} doesn't exist for seller_id: {seller_id}"}
    elif pin in user_pins:
        return {"message": f"{pin} exist for seller_id: {seller_id}"}
    else:
        return {"message": f"Something went wrong"}


@router.post("/create")
def create(user_data: UserPinData):
    seller_id = user_data.seller_id
    pins = user_data.pins
    print('seller_id:', seller_id)

    line_number = find_the_line_number_of_id(seller_id)
    if line_number == -1:
        return {"message": f"{seller_id} doesn't exist in our database"}
    db_conntent_prev = read_specific_line('base.db', line_number)
    # print('db_conntent_prev:', ord(db_conntent_prev), 'line_number:', line_number)
    if len(db_conntent_prev) == 0:
        hashmap_tree = HashMapTree()
        hashmap_tree.insert_empty_tree(seller_id)
        # return {"message": f"{seller_id} already exist in our database"}
    else:
        hashmap_tree = HashMapTree()
        hashmap_tree = reconstruct_tree_from_string(convert_string_to_data(db_conntent_prev), seller_id)


    for pin in pins:
        hashmap_tree.insert_digit(seller_id, pin)
    # for tree in hashmap_tree.hashmap.values():
        
    tree: BinaryTree = hashmap_tree.hashmap[seller_id]
    data = tree.create_data_to_save()
    data_to_save = convert_data_to_string(data)
    # print('line_number:', line_number)
    
    db.add_value_at_line(line_number, data_to_save)
    message = "Pin Inserted Successfully for the user"
            
    return {"message": message}


@router.put("/update")
def update(user_data: UserPinData):
    seller_id = user_data.seller_id
    updated_pins = user_data.pins
    print('seller_id:', seller_id)
    line_number = find_the_line_number_of_id(seller_id)
    print('line_number:', line_number)

    hashmap_tree.insert_empty_tree(seller_id)
    for pin in updated_pins:
        hashmap_tree.insert_digit(seller_id, pin)
    for tree in hashmap_tree.hashmap.values():
        data = tree.create_data_to_save()
        data_to_save = convert_data_to_string(data)
        if line_number == -1:
            return {"message": f"{seller_id} doesn't exist in our database"}
        db.add_value_at_line(line_number, data_to_save)
        message = "Pin Inserted Successfully for the user"
            
    return {"message": message}


@router.delete("/delete")
def delete_user(user_data: UserPinData):
    seller_id = user_data.seller_id
    print('seller_id:', seller_id)

    line_number = find_the_line_number_of_id(seller_id)
    print('line_number:', line_number)
    if line_number == -1:
        return {"message": f"{seller_id} doesn't exist in our database"}
    
    fetch_user_pins = read_user_pins(line_number)
    valid_pins = []
    for pin in user_data.pins:
        ### NOTE: It breaking while reconstructing the binary data and searching for pin in it.
        isFound = check_if_key_exists(fetch_user_pins, pin)
        if isFound:
            valid_pins.append(pin)
        else:
            pass
    if valid_pins.__len__() == 0:
        return {"message": f"{seller_id} doesn't have any valid pins to delete"}
    
    updated_pins = [pin for pin in fetch_user_pins if pin not in valid_pins]
    print('updated_pins:', updated_pins)
    hashmap_tree.insert_empty_tree(seller_id)
    for pin in updated_pins:
        hashmap_tree.insert_digit(seller_id, pin)
    for tree in hashmap_tree.hashmap.values():
        data = tree.create_data_to_save()
        data_to_save = convert_data_to_string(data)
        db.add_value_at_line(line_number, data_to_save)
        message = "Pin Inserted Successfully for the user"
    isFound = check_if_key_exists(fetch_user_pins, 855107)
    print(f"The pins existance is : {isFound}")
    if isFound:
        print("Pin exist")
        updated_pins = [pin for pin in fetch_user_pins if pin not in user_data.pins]
        print('updated_pins:', updated_pins)

        hashmap_tree.insert_empty_tree(seller_id)
        for pin in updated_pins:
            hashmap_tree.insert_digit(seller_id, pin)
        for tree in hashmap_tree.hashmap.values():
            data = tree.create_data_to_save()
            data_to_save = convert_data_to_string(data)
            db.add_value_at_line(line_number, data_to_save)
            message = "Pin Inserted Successfully for the user"
        
        return {"message": message}
    else:
        return {"message": f"{pin} doesn't belong to user: {seller_id}"}