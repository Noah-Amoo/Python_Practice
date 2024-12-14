filename = 'pi_digits.txt'

with open(filename) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))