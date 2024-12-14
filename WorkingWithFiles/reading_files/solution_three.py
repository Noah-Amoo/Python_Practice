filename = 'exercise.txt'

with open(filename) as file:
    lines = file.readlines()

full_text = ''
for line in lines:
    full_text += line.strip() + '\n'

print(full_text)
print(len(full_text))
print(full_text[:10])