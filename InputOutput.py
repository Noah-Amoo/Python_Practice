#                 PYTHON PROGRAMMING TUTORIAL FOR ABSOLUTE BEGINNERS
#                                BY NOAH AMOO

# The print function is used to display text on the screen. You must use parentheses and quotes around the text you want to print.
print("hello world")

# To store data temporarily in a computer's memory, you need a variable.
# To declare a variable, you must give it a name and assign it a value to it using the equals sign (=).
name = "Noah"
print(name)
age = 20
print(age)
print("Hello world. My name is " + name + " and I am " + str(age) + " years old.")

                                    # Types of variables
# Strings: a sequence of characters. You can use either single or double quotes to declare a string.
# Integers: whole numbers. You can use either positive or negative numbers.
# Floats: numbers with a decimal point. You can use either positive or negative numbers.
# Booleans: True or False. You can use either True or False.

first_name = "Nana"
age = 30
salaray = 396,400.99
is_online = True 

                                    # Receiving User Input
# Use the input function to reeive input from the user.
name_of_user = input("What is your name? ")
print("Hello " + name_of_user + ", welcome to the Python programming tutorial.")

                                    #  Type Conversion
# Use the int() function to convert a string to an integer.
# Use the str() function to convert a integer to a string.
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print("Your age in 2024 is " + str(age)) 

# To convert a value to a floating point number, you must use the float() function.
salary = float(salaray)

# To convert a value to a boolean, you must use the bool() function.
is_online = bool(is_online)

                        #EXERCISE 1: BASIC CALCULATOR PROGRAM
#Write a program that receives two numbers from the use and displays the sum of the two numbers.
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
sum = int(first_number) + int(second_number)
print("The sum of the two numbers is " + str(sum))

# To complete the assignment, calculate for the difference, product, and quotient of the two numbers.