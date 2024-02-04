import gzip

# it creates a file of 1KB and only way possible to keep the insertion in 1KB without data loss


class CustomDatabase:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_value_at_line(self, line_number, value):
        print('value here is:', value, 'line number is:',
              line_number, 'type of value:', type(value))
        if line_number < 1:
            raise ValueError(f"Invalid line number: {line_number}")

        try:
            with gzip.open(self.file_path, 'rb') as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        compressed_value = gzip.compress(str(value).encode('utf-8')) + b'\n'

        if line_number <= len(lines):
            lines = lines[:line_number - 1] + \
                [compressed_value] + lines[line_number:]
        else:
            lines += [b'\n'] * (line_number - len(lines) - 1)
            lines.append(compressed_value)

        with gzip.open(self.file_path, 'wb') as file:
            file.writelines(lines)

    def get_value(self, line_number):
        try:
            with gzip.open(self.file_path, 'rb') as file:
                for _ in range(line_number):
                    line_data = file.readline()
                    if not line_data:
                        break

                if not line_data:
                    raise ValueError(
                        f"Invalid line number: {line_number}, file ends at line {file.tell()}")

                decompressed_value = gzip.decompress(line_data.rstrip(b'\r\n'))

                return decompressed_value.decode('utf-8')

        except FileNotFoundError:
            raise LookupError(f"File '{self.file_path}' not found")
