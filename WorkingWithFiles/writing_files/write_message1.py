filename = 'programming.txt'

#The second argument r+ means to open the file for reading and writing
#In this case, the parameter is 'w' which means to open the file for writing
#Remember that python can only write strings to a text file
with open(filename, 'w') as file:
    file.write('I love programming!\n')
    file.write('I love creatingn web applications!\n')