from collections import defaultdict
import os
import sys
import hashlib


if len(sys.argv) < 2:
    print("Directory is not specified")
    exit()


# Program's start
root_dir = sys.argv[1]
os.chdir(root_dir)
full_path = os.getcwd()
file_sizes = defaultdict(set)
file_hashes = defaultdict(list)
duplicates = defaultdict(dict)


def input_sorting_option() -> str:
    print("""\
Size sorting options:
1. Descending
2. Ascending""")
    while True:
        sorting_option = input("\nEnter a sorting option:\n")
        if sorting_option in ('1', '2'):
            break
        else:
            print("\nWrong option\n")
    return sorting_option


def collect_file_sizes():
    for root, dirs, files in os.walk(full_path):
        for name in files:
            if file_format:
                current_format = os.path.splitext(name)[-1].replace('.', '')
                if current_format != file_format:
                    continue
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            file_sizes[file_size].add(file_path)


def print_size(size):
    print(f'\n{size} bytes')


def print_file_sizes():
    for size, files in sorted(file_sizes.items(), reverse=descending_sorting):
        if len(files) > 1:
            print_size(size)
            for file_name in files:
                print(file_name)
        else:
            file_sizes.pop(size)


def ask_for_duplicates_checking():
    if file_sizes:
        user_input = input("Check for duplicates?\n")
        while user_input not in ("yes", "no"):
            print("Wrong option")
        if user_input == "no":
            exit()


def get_file_hash(file_path):
    md5hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        chunk = None
        while chunk != b'':
            chunk = file.read(1024)
            md5hash.update(chunk)
    return md5hash.hexdigest()


def collect_hashes():
    for size, files in file_sizes.items():
        for file_name in files:
            file_hash = get_file_hash(file_name)
            if not duplicates[size].get(file_hash):
                duplicates[size][file_hash] = []
            duplicates[size][file_hash].append(file_name)


def print_duplicates():
    index = 1
    for file_size, hashes in sorted(duplicates.items(), reverse=descending_sorting):
        size_printed = False
        for file_hash, file_names in hashes.items():
            if len(file_names) < 2:
                continue
            if not size_printed:
                print_size(file_size)
                size_printed = True
            print(f"Hash: {file_hash}")
            for file_name in file_names:
                print(f"{index}. {file_name}")
                index += 1


file_format = input("Enter file format:\n")
descending_sorting: bool = input_sorting_option() == '1'
collect_file_sizes()
print_file_sizes()
ask_for_duplicates_checking()
collect_hashes()
print_duplicates()
