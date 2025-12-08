# Lesson 1: Python Basics
# This file covers the fundamental concepts of Python programming

# =====================================
# 1. COMMENTS AND DOCUMENTATION
# =====================================

# This is a single-line comment
# Use comments to explain your code

"""
This is a multi-line comment (docstring)
You can write longer explanations here
"""

print("Welcome to Python! Let's learn the basics.")
print()  # Print an empty line for spacing

# =====================================
# 2. VARIABLES AND DATA TYPES
# =====================================

print("=== VARIABLES AND DATA TYPES ===")

# Variables store data - think of them as labeled boxes
name = "Alice"           # String (text)
age = 25                 # Integer (whole number)
height = 5.6             # Float (decimal number)
is_student = True        # Boolean (True/False)

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")

# You can check the type of any variable
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print()

# =====================================
# 3. BASIC OPERATIONS
# =====================================

print("=== BASIC OPERATIONS ===")

# Math operations
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer division: {a} // {b} = {a // b}")
print(f"Remainder (modulo): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print()

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
print(f"Full name: {full_name}")
print(f"Name in uppercase: {full_name.upper()}")
print(f"Name in lowercase: {full_name.lower()}")
print(f"Length of name: {len(full_name)}")
print()

# =====================================
# 4. USER INPUT
# =====================================

print("=== USER INPUT ===")

# Get input from the user
print("Let's get to know you!")
user_name = input("What's your name? ")
user_age = input("How old are you? ")

# Note: input() always returns a string, so we convert to int if needed
user_age_number = int(user_age)

print(f"Hello {user_name}! You are {user_age_number} years old.")
print(f"Next year you will be {user_age_number + 1} years old.")
print()

# =====================================
# 5. STRING FORMATTING
# =====================================

print("=== STRING FORMATTING ===")

# Different ways to format strings
product = "laptop"
price = 999.99
quantity = 2

# Method 1: f-strings (recommended)
message1 = f"You bought {quantity} {product}s for ${price:.2f} each"

# Method 2: .format() method
message2 = "You bought {} {}s for ${:.2f} each".format(quantity, product, price)

# Method 3: % formatting (older style)
message3 = "You bought %d %ss for $%.2f each" % (quantity, product, price)

print("Method 1 (f-string):", message1)
print("Method 2 (.format()):", message2)
print("Method 3 (% format):", message3)
print()

# =====================================
# 6. VARIABLE ASSIGNMENT TRICKS
# =====================================

print("=== VARIABLE ASSIGNMENT TRICKS ===")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Swapping variables
x, y = y, x
print(f"After swapping: x = {x}, y = {y}")

# Same value to multiple variables
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")
print()

# =====================================
# 7. PRACTICE EXERCISES
# =====================================

print("=== PRACTICE TIME! ===")
print("Try these exercises:")
print("1. Create variables for your favorite movie, year it was made, and rating (1-10)")
print("2. Calculate and print how many years ago the movie was made")
print("3. Create a formatted message about the movie")
print()

# Example solution (uncomment to see):
# movie = "The Shawshank Redemption"
# year = 1994
# rating = 9.5
# current_year = 2024
# years_ago = current_year - year
# 
# print(f"My favorite movie is '{movie}' from {year}.")
# print(f"It was made {years_ago} years ago and I rate it {rating}/10!")

print("Great job completing Lesson 1! 🎉")
print("Next up: Lesson 2 - Control Structures")