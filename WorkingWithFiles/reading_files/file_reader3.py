filename = 'pi_digits.txt'

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())