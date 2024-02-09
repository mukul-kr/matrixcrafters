import os


class CustomDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        # Open a file in write mode ('w')
        if not os.path.exists('base.db'):
            with open('base.db', 'w') as file:
                # Write '\n'  10 million times
                for _ in range(10000000):
                    file.write('\n')

    def add_value_at_line(self, line_number, value):
        print('value here is:', value, 'line number is:',
              line_number, 'type of value:', type(value))
        if line_number < 1:
            raise ValueError(f"Invalid line number: {line_number}")

        try:
            with open(self.file_path, 'rb') as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        new_line = str(value).encode('utf-8') + b'\n'

        if line_number <= len(lines):
            lines = lines[:line_number - 1] + [new_line] + lines[line_number:]
        else:
            lines += [b'\n'] * (line_number - len(lines) - 1)
            lines.append(new_line)

        with open(self.file_path, 'wb') as file:
            file.writelines(lines)

    def get_value(self, line_number):
        try:
            with open(self.file_path, 'rb') as file:
                for _ in range(line_number):
                    line_data = file.readline()
                    if not line_data:
                        break

                if not line_data:
                    raise ValueError(
                        f"Invalid line number: {line_number}, file ends at line {file.tell()}")

                value = line_data.rstrip(b'\r\n').decode('utf-8')

                return value

        except FileNotFoundError:
            raise LookupError(f"File '{self.file_path}' not found")

db = CustomDatabase("base.db")