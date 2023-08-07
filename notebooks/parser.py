import my_format

def parse_binary_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    offset = 0
    instances = []

    while offset < len(data):
        parsed_data = my_format.from_bytes(data[offset:])
        instances.append(parsed_data)
        offset += parsed_data._io.size()  # Move offset by the parsed instance size

    return instances

if __name__ == "__main__":
    binary_file_path = "your_binary_file.bin"
    parsed_instances = parse_binary_file(binary_file_path)

    for idx, instance in enumerate(parsed_instances, start=1):
        print(f"Instance {idx}:")
        print("Magic Number:", hex(instance.magic))
        print("Version:", instance.version)
        print("Data Size:", instance.data_size)
        print("Data:", instance.data)
        print()