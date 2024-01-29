import random
import string

def generate_random_id(length):
    characters = string.digits + string.ascii_lowercase[:6]
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id

def generate_unique_ids(set_size, id_length):
    unique_ids = set()

    while len(unique_ids) < set_size:
        random_id = generate_random_id(id_length)
        unique_ids.add(random_id)

    return sorted(unique_ids)

set_size = 10000 # 10000000
id_length = 6

unique_ids = generate_unique_ids(set_size, id_length)

with open('id.txt', 'w') as file:
    for unique_id in unique_ids:
        file.write(unique_id + '\n')
