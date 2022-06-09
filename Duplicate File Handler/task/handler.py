import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description='In this stage, we start by identifying files of the same size in bytes.')
    parser.add_argument("root_directory", nargs='?', default=None)
    args = parser.parse_args()

    if args.root_directory is None:
        print("Directory is not specified")
        sys.exit()

    all_files = []
    for root, dirs, files in os.walk(args.root_directory):
        for name in files:
            file = os.path.join(root, name)
            all_files.append(file)

    print('Enter file format:')
    file_format = input()

    print('\nSize sorting options:\n1. Descending\n2. Ascending\n')

    while True:
        print('Enter a sorting option:')
        sorting_option = input()

        if sorting_option in ['1', '2']:
            if sorting_option == '1':
                ascending = False
            else:
                ascending = True
            break
        print('Wrong option')

    dict_size_file = dict()

    if not file_format:
        for file in all_files:
            file_size = str(os.path.getsize(file))
            if file_size not in dict_size_file:
                dict_size_file[file_size] = list()
            dict_size_file[file_size].append(file)

    sorted_dict_keys = [int(x) for x in dict_size_file.keys()]

    if ascending:
        sorted_dict_keys.sort()
    else:
        sorted_dict_keys.sort(reverse=True)

    sorted_dict_keys = [str(x) for x in sorted_dict_keys]

    for key in sorted_dict_keys:
        print(key, 'bytes')
        for value in dict_size_file[key]:
            print(value)


if __name__ == '__main__':
    main()
