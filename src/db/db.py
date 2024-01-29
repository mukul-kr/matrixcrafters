import struct

class CustomDatabase:
    def __init__(self, file_path):
        self.file_path = file_path

    def _serialize_key_value(self, key, value):
        key_bytes = key.encode('utf-8')
        value_bytes = struct.pack('h', value) if value is not None else struct.pack('h', -1)
        return b'\x01' + key_bytes + b'\x02' + value_bytes + b'\x99' + b'\x98'

    def _deserialize_key_value(self, data):
        key_start = data.find(b'\x01') + 1
        key_end = data.find(b'\x02')
        value_start = key_end + 1
        value_end = data.find(b'\x99', value_start)

        key = data[key_start:key_end].decode('utf-8')

        # Check if there are at least 2 bytes for unpacking a short integer
        if value_end - value_start >= 2:
            value = struct.unpack('h', data[value_start:value_end])[0]
            if value < 0:
                value = None
            return key, value
        else:
            # Handle the case where there are not enough bytes for value unpacking
            return key, None


    def add_key_value(self, key, value):
        # Read existing data
        try:
            with open(self.file_path, 'rb') as file:
                existing_data = file.read()
        except FileNotFoundError:
            existing_data = b''

        # Serialize new key-value pair
        new_data = self._serialize_key_value(key, value)

        # Write combined data to the file
        with open(self.file_path, 'wb') as file:
            file.write(existing_data + new_data)

    def get_value(self, key):
        try:
            with open(self.file_path, 'rb') as file:
                data = file.read()

            # Iterate through the binary data to find the matching key
            data_list = data.split(b'\x98')
            for i in range(len(data_list)):
                
                current_key, current_value = self._deserialize_key_value(data_list[i])
                if current_key == key:
                    return current_value
                
                # index += len(self._serialize_key_value(current_key, current_value))

            # Key not found
            raise LookupError(f"Key '{key}' not found")

        except FileNotFoundError:
            # File doesn't exist, return None
            raise LookupError(f"File '{self.file_path}' not found")

# Example usage:
db = CustomDatabase("db.bin")

# Add key-value pairs
db.add_key_value("name", 0)
db.add_key_value("age", 1)
db.add_key_value("city", 2)
db.add_key_value("some3", 3)
db.add_key_value("some4", 4)
db.add_key_value("some5", 5)
db.add_key_value("some6", 6)
db.add_key_value("some7", 7)
db.add_key_value("some8", 8)
db.add_key_value("some9", 9)
db.add_key_value("none", None)


# Retrieve values
print("Value for 'name':", db.get_value("name"))
print("Value for 'age':", db.get_value("age"))
print("Value for 'city':", db.get_value("city"))
print("Value for 'some3':", db.get_value("some3"))
print("Value for 'some4':", db.get_value("some4"))
print("Value for 'some5':", db.get_value("some5"))
print("Value for 'some6':", db.get_value("some6"))
print("Value for 'some7':", db.get_value("some7"))
print("Value for 'some8':", db.get_value("some8"))
print("Value for 'some9':", db.get_value("some9"))
print("Value for 'none':", db.get_value("none"))
print("Value for 'unknown_key':", db.get_value("unknown_key"))