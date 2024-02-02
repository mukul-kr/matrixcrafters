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
