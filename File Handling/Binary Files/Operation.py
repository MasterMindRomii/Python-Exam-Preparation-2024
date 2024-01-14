def create_binary_file(filename):
    file = open(filename, "wb")
    file.close()
    print(f"Binary file '{filename}' created successfully.")


# Example usage:
binary_filename = "example_binary_create.dat"
create_binary_file(binary_filename)


def write_to_binary_file(filename, data):
    file = open(filename, "wb")
    file.write(data)
    file.close()
    print(f"Data written to binary file '{filename}' successfully.")


# Example usage:
binary_filename = "example_binary_write.dat"
binary_data = b"\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64"  # Binary representation of "Hello, World"
write_to_binary_file(binary_filename, binary_data)


def read_from_binary_file(filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    print(f"Data read from binary file '{filename}': {data}")
    return data


# Example usage:
binary_filename = "example_binary_write.dat"
read_from_binary_file(binary_filename)
