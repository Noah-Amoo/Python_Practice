# Replace the word 'Python' with the word 'Java'

filename = 'exercise.txt'

with open(filename) as file:
    content = file.read()
    content = content.replace('Python', 'Java')
    print(content)