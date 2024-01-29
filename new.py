# with open('my_custom_db.bin', 'rb') as file:
#     existing_data = file.read()
#     print(existing_data)
    # key_length = len(data) - 1
    # key = data[:key_length].decode('utf-8')
    # value = struct.unpack('!B', data[key_length:])[0]


import struct

import struct

def serialize_key_value(key, value):
    key_bytes = key.encode('utf-8')
    value_bytes = struct.pack('h', value)
    return b'\x01' + key_bytes + b'\x02' + value_bytes + b'\x03'

def deserialize_key_value(data):
    key_start = data.find(b'\x01') + 1
    key_end = data.find(b'\x02')
    value_start = key_end + 1
    value_end = data.find(b'\x03')

    key = data[key_start:key_end].decode('utf-8')
    value = struct.unpack('h', data[value_start:value_end])[0]

    return key, value

# Example usage:
something = serialize_key_value("a", 2)
print(deserialize_key_value(something))

# print(struct.pack('c', b'0'))
print(struct.calcsize('h'))