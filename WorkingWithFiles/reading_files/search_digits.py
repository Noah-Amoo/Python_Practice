filename = 'pi_digits.txt'

with open(filename) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday in the format ddmmyy: ')
if birthday in pi_string:
    print('You have a birthday that is a pi digit!')
else:
    print('You do not have a birthday that is a pi digit!')