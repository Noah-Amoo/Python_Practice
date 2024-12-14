filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print(f'The file {filename} does not exist!')
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} contains {num_words} words")