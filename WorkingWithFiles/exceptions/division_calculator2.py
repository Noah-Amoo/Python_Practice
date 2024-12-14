print("Give me two numbers and I'lll divide them!")
print("Enter 'q' to quit")

while True:
    try:
        first_number = input('Enter the first number:')
        if first_number == 'q':
            break
        second_number = input('Enter the second number: ')
        if second_number == 'q':
            break
        answer = int(first_number) / int(second_number)
        print(f'The answer is {answer}')
    except ValueError:
        print('You must enter a number!')
    except ZeroDivisionError:
        print('You cannot divide by zero!')