filename = 'programmer_responses.txt'

with open(filename, 'a') as file:
    while True:
        user_input = input('Why do you love programming? \n')
        if user_input == 'q':
            break
        file.write(f"{user_input}\n")