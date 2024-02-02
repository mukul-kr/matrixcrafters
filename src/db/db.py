import struct


class CustomDatabase:
    def __init__(self, file_path):
        self.file_path = file_path

    def _serialize_value(self, value):
        # use a prefix byte to indicate the type of the value
        # b'\x01' for int, b'\x02' for str, b'\x00' for None
        if isinstance(value, int):
            return b'\x01' + self._serialize_int_value(value)
        elif isinstance(value, str):
            return b'\x02' + self._serialize_str_value(value)
        elif value is None:
            return b'\x00'
        else:
            raise ValueError(
                "Unsupported value type. Only int, str and None are supported.")

    def _serialize_int_value(self, value):
        return struct.pack('h', value)

    def _serialize_str_value(self, value):
        return value.encode('utf-8')

    def _deserialize_value(self, data):
        # use the prefix byte to determine the type of the value
        # b'\x01' for int, b'\x02' for str, b'\x00' for None
        prefix = data[0]
        if bytes([prefix]) == b'\x01':
            return self._deserialize_int_value(data[1:])
        elif bytes([prefix]) == b'\x02':
            return self._deserialize_str_value(data[1:])
        elif bytes([prefix]) == b'\x00':
            return None
        else:
            raise ValueError(
                "Invalid prefix byte. Expected b'\x01', b'\x02' or b'\x00'")

    def _deserialize_int_value(self, data):
        return struct.unpack('h', data)[0]

    def _deserialize_str_value(self, data):
        return data.decode('utf-8')

    def add_value_at_line(self, line_number, value):
        if line_number < 1:
            raise ValueError(f"Invalid line number: {line_number}")

        new_data = self._serialize_value(value)

        try:
            with open(self.file_path, 'rb') as file:
                existing_data = file.read()
        except FileNotFoundError:
            existing_data = b''

        data_lines = existing_data.split(b'\n')

        if line_number <= len(data_lines):
            data_lines[line_number - 1] = new_data
        else:
            data_lines += [b''] * (line_number - len(data_lines) - 1)
            data_lines.append(new_data)

        new_binary_data = b'\n'.join(data_lines)

        with open(self.file_path, 'wb') as file:
            file.write(new_binary_data)

    def get_value(self, line_number):
        try:
            with open(self.file_path, 'rb') as file:
                for _ in range(line_number - 1):
                    file.readline()
                line_data = file.readline().rstrip(b'\r\n')
                if not line_data:
                    raise ValueError(
                        f"Invalid line number: {line_number}, file ends at line {file.tell()}")

                value = self._deserialize_value(line_data)

                return value

        except FileNotFoundError:
            raise LookupError(f"File '{self.file_path}' not found")
