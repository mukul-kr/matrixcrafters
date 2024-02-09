
from fastapi import APIRouter, Query
from src.data_structure.binary_tree import BinaryTree
from src.data_structure.hash_map_tree import HashMapTree
from src.db.db import db

from src.helper.utils import convert_data_to_string, convert_string_to_data, find_the_line_number_of_id, read_specific_line, read_user_pins, reconstruct_tree_from_string
from src.routes.schema import DeleteUserPinData, UpdateUserPinData, UserPinData

router = APIRouter()


@router.get("/health_check")
def health_check():
    return {"status": "OK"}


@router.get("/search")
def search(seller_id: str = Query(..., alias="seller_id"), pin: str = Query(...)):
    line_number = find_the_line_number_of_id(seller_id)
    if line_number == -1:
        return {"message": f"{seller_id} doesn't exist in our database"}
    db_conntent_prev = read_specific_line('base.db', line_number)
    
    hashmap_tree = reconstruct_tree_from_string(
        convert_string_to_data(db_conntent_prev), seller_id)
    fetch_user_pins = read_user_pins(hashmap_tree)
    print(fetch_user_pins, 'The user have these pins associated to them')

    user_pins = [pin for pin in fetch_user_pins]
    if pin not in user_pins:
        return {
            "message": f"{pin} doesn't exist for seller_id: {seller_id}", 
            "exists": False
            }
    elif pin in user_pins:
        return {
            "message": f"{pin} exist for seller_id: {seller_id}",
            "exists": True
            }
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
    print('db_conntent_prev:', db_conntent_prev, 'line_number:', line_number)
    if True:
        hashmap_tree = HashMapTree()
        hashmap_tree.insert_empty_tree(seller_id)
        # return {"message": f"{seller_id} already exist in our database"}
    else:
        # hashmap_tree = HashMapTree()
        hashmap_tree = reconstruct_tree_from_string(
            convert_string_to_data(db_conntent_prev), seller_id)
        hashmap_tree.print_all_trees()

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
def update(user_data: UpdateUserPinData):
    seller_id = user_data.seller_id
    old_pin = user_data.old_pin
    new_pin = user_data.new_pin
    line_number = find_the_line_number_of_id(seller_id)
    if line_number == -1:
        return {"message": f"{seller_id} doesn't exist in our database"}
    db_conntent_prev = read_specific_line('base.db', line_number)
    hashmap_tree = reconstruct_tree_from_string(
        convert_string_to_data(db_conntent_prev), seller_id)
    fetch_user_pins = read_user_pins(hashmap_tree)
    print(fetch_user_pins, 'The user have these pins associated to them')
    if old_pin not in fetch_user_pins:
        return {"message": f"{old_pin} doesn't exist for seller_id: {seller_id}"}
    elif old_pin in fetch_user_pins:
        updated_pins = [new_pin if pin == old_pin else pin for pin in fetch_user_pins]
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
        return {"message": f"{old_pin} doesn't belong to user: {seller_id}"}


@router.delete("/delete")
def delete_user(user_data: DeleteUserPinData):
    seller_id = user_data.seller_id
    pin_to_delete = user_data.pin
    line_number = find_the_line_number_of_id(seller_id)
    if line_number == -1:
        return {"message": f"{seller_id} doesn't exist in our database"}
    db_conntent_prev = read_specific_line('base.db', line_number)
    hashmap_tree = reconstruct_tree_from_string(
        convert_string_to_data(db_conntent_prev), seller_id)
    fetch_user_pins = read_user_pins(hashmap_tree)
    print(fetch_user_pins, 'The user have these pins associated to them')
    if pin_to_delete not in fetch_user_pins:
        return {"message": f"{pin_to_delete} doesn't exist for seller_id: {seller_id}"}
    elif pin_to_delete in fetch_user_pins:
        updated_pins = [pin for pin in fetch_user_pins if pin != pin_to_delete]
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
        return {"message": f"{pin_to_delete} doesn't belong to user: {seller_id}"}