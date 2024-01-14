# Creation of text file 
def create_file(filename):
    file = open(filename, 'w')
    file.close()
    print(f"File '{filename}' created successfully.")

# Example usage:
filename = "example_create.txt"
create_file(filename)

# Write of text file 
def write_to_file(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()
    print(f"Data written to '{filename}' successfully.")

# Example usage:
filename = "example_write.txt"
data = "Hello, this is line 1.\nThis is line 2.\n"
write_to_file(filename, data)

# Append of text file 
def append_to_file(filename, data):
    file = open(filename, 'a')
    file.write(data)
    file.close()
    print(f"Data appended to '{filename}' successfully.")

# Example usage:
filename = "example_append.txt"
data = "Appending to line 3.\n"
append_to_file(filename, data)

# Insert to text file
def insert_into_file(filename, line_number, data):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    lines.insert(line_number - 1, data + '\n')

    file = open(filename, 'w')
    file.writelines(lines)
    file.close()

    print(f"Data inserted into '{filename}' at line {line_number} successfully.")

# Example usage:
filename = "example_insert.txt"
line_number = 2
data = "Inserting at line 2."
insert_into_file(filename, line_number, data)

# Delete of text file 
def delete_from_file(filename, line_number):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    if 1 <= line_number <= len(lines):
        deleted_data = lines.pop(line_number - 1)

        file = open(filename, 'w')
        file.writelines(lines)
        file.close()

        print(f"Data deleted from '{filename}' at line {line_number}: {deleted_data}")
    else:
        print(f"Invalid line number: {line_number}")

# Example usage:
filename = "example_delete.txt"
line_number = 3
delete_from_file(filename, line_number)

# Update of text file 
def update_file(filename, line_number, new_data):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    if 1 <= line_number <= len(lines):
        old_data = lines[line_number - 1]
        lines[line_number - 1] = new_data + '\n'

        file = open(filename, 'w')
        file.writelines(lines)
        file.close()

        print(f"Data updated in '{filename}' at line {line_number}.")
        print(f"Old data: {old_data.strip()}")
        print(f"New data: {new_data}")
    else:
        print(f"Invalid line number: {line_number}")

# Example usage:
filename = "example_update.txt"
line_number = 1
new_data = "Updated line 1."
update_file(filename, line_number, new_data)
