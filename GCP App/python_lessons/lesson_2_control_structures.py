# Lesson 2: Control Structures
# This file covers if statements, loops, and conditional logic

print("=== LESSON 2: CONTROL STRUCTURES ===")
print("Learning to make decisions and repeat actions in Python")
print()

# =====================================
# 1. IF STATEMENTS
# =====================================

print("=== IF STATEMENTS ===")

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult!")

# if-else statement
score = 85
if score >= 90:
    print("Excellent! You got an A!")
else:
    print("Good job, but there's room for improvement.")

# if-elif-else statement
temperature = 75

if temperature > 80:
    print("It's hot outside! 🌞")
elif temperature > 60:
    print("Nice weather! 🌤️")
elif temperature > 40:
    print("It's a bit cool. 🌥️")
else:
    print("It's cold! ❄️")

print()

# =====================================
# 2. COMPARISON OPERATORS
# =====================================

print("=== COMPARISON OPERATORS ===")

x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater than or equal to
print(f"x <= y: {x <= y}")  # Less than or equal to
print()

# =====================================
# 3. LOGICAL OPERATORS
# =====================================

print("=== LOGICAL OPERATORS ===")

# and, or, not
has_license = True
is_over_16 = True
has_car = False

# Using 'and' - all conditions must be True
can_drive_alone = has_license and is_over_16
print(f"Can drive alone: {can_drive_alone}")

# Using 'or' - at least one condition must be True
can_get_somewhere = has_car or has_license
print(f"Can get somewhere: {can_get_somewhere}")

# Using 'not' - reverses the boolean value
cannot_drive = not has_license
print(f"Cannot drive: {cannot_drive}")

# Complex conditions
weather = "sunny"
has_umbrella = False

if weather == "rainy" and not has_umbrella:
    print("You should take an umbrella!")
elif weather == "sunny" or weather == "cloudy":
    print("Great day to go outside!")
else:
    print("Check the weather before going out.")

print()

# =====================================
# 4. FOR LOOPS
# =====================================

print("=== FOR LOOPS ===")

# Loop through a range of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(start, stop)
    print(f"Number: {i}")

print()

# Loop through a string
print("Letters in 'Python':")
for letter in "Python":
    print(f"Letter: {letter}")

print()

# Loop through a list
fruits = ["apple", "banana", "orange", "grape"]
print("My favorite fruits:")
for fruit in fruits:
    print(f"- {fruit}")

print()

# Using range with different parameters
print("Even numbers from 0 to 10:")
for num in range(0, 11, 2):  # range(start, stop, step)
    print(num, end=" ")  # Print on same line
print()  # New line
print()

# =====================================
# 5. WHILE LOOPS
# =====================================

print("=== WHILE LOOPS ===")

# Basic while loop
countdown = 5
print("Countdown:")
while countdown > 0:
    print(f"{countdown}...")
    countdown = countdown - 1  # Same as: countdown -= 1
print("Blast off! 🚀")
print()

# While loop with user input simulation
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}: Trying to connect...")
    if attempts == 2:  # Simulate success on 2nd attempt
        print("Connected successfully!")
        break  # Exit the loop
    if attempts < max_attempts:
        print("Failed. Retrying...")
else:
    # This runs if loop completes without 'break'
    print("Failed to connect after all attempts.")

print()

# =====================================
# 6. LOOP CONTROL STATEMENTS
# =====================================

print("=== LOOP CONTROL STATEMENTS ===")

# 'continue' - skip the rest of current iteration
print("Odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:  # If even number
        continue      # Skip to next iteration
    print(num, end=" ")
print()
print()

# 'break' - exit the loop completely
print("Finding the first number divisible by 7:")
for num in range(1, 50):
    if num % 7 == 0:
        print(f"Found it: {num}")
        break
print()

# =====================================
# 7. NESTED LOOPS
# =====================================

print("=== NESTED LOOPS ===")

# Multiplication table
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} × {j} = {result}")
    print()  # Empty line after each row

# =====================================
# 8. PRACTICAL EXAMPLES
# =====================================

print("=== PRACTICAL EXAMPLES ===")

# Grade calculator
print("Grade Calculator:")
scores = [85, 92, 78, 96, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f"Scores: {scores}")
print(f"Average: {average:.1f}")

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Final Grade: {grade}")
print()

# Number guessing game simulation
print("Number Guessing Game (Simulated):")
secret_number = 7
guesses = [5, 8, 7]  # Simulated guesses
attempts = 0
max_attempts = 3

for guess in guesses:
    attempts += 1
    print(f"Attempt {attempts}: Guessed {guess}")
    
    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
        
    if attempts >= max_attempts:
        print(f"Game over! The number was {secret_number}")
        break

print()

# =====================================
# 9. EXERCISES FOR PRACTICE
# =====================================

print("=== PRACTICE EXERCISES ===")
print("Try these exercises:")
print("1. Write a program that prints all even numbers from 1 to 20")
print("2. Create a program that counts vowels in a word")
print("3. Write a simple password validator")
print("4. Create a program that finds the largest number in a list")
print()

# Example solutions (uncomment to see):
# 
# # Exercise 1: Even numbers
# print("Even numbers from 1 to 20:")
# for num in range(2, 21, 2):
#     print(num, end=" ")
# print()
# 
# # Exercise 2: Count vowels
# word = "programming"
# vowels = "aeiou"
# count = 0
# for letter in word:
#     if letter.lower() in vowels:
#         count += 1
# print(f"The word '{word}' has {count} vowels")
# 
# # Exercise 3: Password validator
# password = "Python123"
# has_upper = False
# has_number = False
# 
# for char in password:
#     if char.isupper():
#         has_upper = True
#     if char.isdigit():
#         has_number = True
# 
# if len(password) >= 8 and has_upper and has_number:
#     print("Strong password!")
# else:
#     print("Weak password. Needs 8+ chars, uppercase, and number.")

print("Great job completing Lesson 2! 🎉")
print("Next up: Lesson 3 - Functions and Modules")