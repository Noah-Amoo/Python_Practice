filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f'The file {filename} does not exist!')