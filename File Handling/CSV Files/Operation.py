import csv


def create_csv_file(filename, header):
    csvfile = open(filename, "w", newline="")
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    csvfile.close()
    print(f"CSV file '{filename}' created successfully.")


# Example usage:
csv_filename = "example_csv_create.csv"
csv_header = ["Name", "Age", "City"]
create_csv_file(csv_filename, csv_header)


def write_to_csv_file(filename, data):
    csvfile = open(filename, "w", newline="")
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)
    csvfile.close()
    print(f"Data written to CSV file '{filename}' successfully.")


# Example usage:
csv_filename = "example_csv_write.csv"
csv_data = [["John", 25, "New York"], ["Jane", 30, "Los Angeles"]]
write_to_csv_file(csv_filename, csv_data)


def read_from_csv_file(filename):
    csvfile = open(filename, "r")
    csv_reader = csv.reader(csvfile)
    data = [row for row in csv_reader]
    csvfile.close()
    print(f"Data read from CSV file '{filename}': {data}")
    return data


# Example usage:
csv_filename = "example_csv_write.csv"
read_from_csv_file(csv_filename)
