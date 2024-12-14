filename = 'guest_book.txt'

print('Please enter guest names\n')
print('Type "q" when you are done\n')

with open(filename, 'w') as file:
    while True:
        name = input("Enter your name: ")
        if name == 'q':
            break
        print(f"Hello {name}!")
        file.write(f"{name}\n")