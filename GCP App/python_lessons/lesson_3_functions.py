# Lesson 3: Functions and Modules
# This file covers creating functions, parameters, return values, and imports

print("=== LESSON 3: FUNCTIONS AND MODULES ===")
print("Learning to organize code into reusable functions")
print()

# =====================================
# 1. BASIC FUNCTIONS
# =====================================

print("=== BASIC FUNCTIONS ===")

# Define a simple function
def greet():
    """This function greets someone."""
    print("Hello, welcome to Python!")

# Call the function
greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person by name."""
    print(f"Hello, {name}! Nice to meet you!")

greet_person("Alice")
greet_person("Bob")
print()

# =====================================
# 2. FUNCTIONS WITH RETURN VALUES
# =====================================

print("=== FUNCTIONS WITH RETURN VALUES ===")

# Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result

# Use the returned value
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 20)
print(f"5 + 3 = {sum1}")
print(f"10 + 20 = {sum2}")

# Function that returns multiple values
def get_name_info(full_name):
    """Split a full name and return first and last name."""
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]  # Last element
    return first_name, last_name

# Unpack multiple return values
first, last = get_name_info("John Smith")
print(f"First name: {first}, Last name: {last}")
print()

# =====================================
# 3. DEFAULT PARAMETERS
# =====================================

print("=== DEFAULT PARAMETERS ===")

def introduce(name, age=25, city="Unknown"):
    """Introduce someone with optional age and city."""
    print(f"Hi, I'm {name}. I'm {age} years old and I live in {city}.")

# Call with different numbers of arguments
introduce("Alice")
introduce("Bob", 30)
introduce("Carol", 28, "New York")
print()

# =====================================
# 4. KEYWORD ARGUMENTS
# =====================================

print("=== KEYWORD ARGUMENTS ===")

def create_profile(name, age, city, occupation="Student"):
    """Create a user profile."""
    print(f"Profile: {name}, {age} years old, {occupation} from {city}")

# Call with keyword arguments (order doesn't matter)
create_profile(age=22, name="David", city="London")
create_profile(name="Emma", city="Paris", age=25, occupation="Engineer")
print()

# =====================================
# 5. VARIABLE-LENGTH ARGUMENTS
# =====================================

print("=== VARIABLE-LENGTH ARGUMENTS ===")

# *args - for variable positional arguments
def calculate_sum(*numbers):
    """Calculate sum of any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {calculate_sum(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {calculate_sum(1, 2, 3, 4, 5)}")

# **kwargs - for variable keyword arguments
def print_info(**info):
    """Print key-value pairs."""
    for key, value in info.items():
        print(f"{key}: {value}")

print("\nStudent information:")
print_info(name="Alice", age=20, major="Computer Science", gpa=3.8)
print()

# =====================================
# 6. LOCAL VS GLOBAL SCOPE
# =====================================

print("=== VARIABLE SCOPE ===")

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error!

# Modifying global variables
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter is now: {counter}")

increment()
increment()
print()

# =====================================
# 7. LAMBDA FUNCTIONS
# =====================================

print("=== LAMBDA FUNCTIONS ===")

# Lambda function (anonymous function)
square = lambda x: x ** 2
double = lambda x: x * 2

print(f"Square of 5: {square(5)}")
print(f"Double of 7: {double(7)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"Add 3 + 4: {add(3, 4)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")
print()

# =====================================
# 8. BUILT-IN FUNCTIONS
# =====================================

print("=== USEFUL BUILT-IN FUNCTIONS ===")

numbers = [10, 5, 8, 20, 3]

print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sorted: {sorted(numbers)}")

# String functions
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print()

# =====================================
# 9. PRACTICAL FUNCTION EXAMPLES
# =====================================

print("=== PRACTICAL EXAMPLES ===")

def calculate_grade(scores):
    """Calculate letter grade from a list of scores."""
    if not scores:  # Check if list is empty
        return "No scores provided"
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        return f"A ({average:.1f}%)"
    elif average >= 80:
        return f"B ({average:.1f}%)"
    elif average >= 70:
        return f"C ({average:.1f}%)"
    elif average >= 60:
        return f"D ({average:.1f}%)"
    else:
        return f"F ({average:.1f}%)"

# Test the function
student_scores = [85, 92, 78, 96, 88]
grade = calculate_grade(student_scores)
print(f"Student grades: {student_scores}")
print(f"Final grade: {grade}")

def is_palindrome(text):
    """Check if a string is a palindrome (reads same forwards and backwards)."""
    # Clean the text (remove spaces, convert to lowercase)
    cleaned = text.replace(" ", "").lower()
    # Compare with its reverse
    return cleaned == cleaned[::-1]

# Test palindrome function
words = ["racecar", "hello", "A man a plan a canal Panama"]
for word in words:
    result = is_palindrome(word)
    print(f"'{word}' is palindrome: {result}")

print()

def fibonacci(n):
    """Generate the first n numbers in the Fibonacci sequence."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence

# Test Fibonacci function
fib_nums = fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_nums}")
print()

# =====================================
# 10. IMPORTING MODULES
# =====================================

print("=== IMPORTING MODULES ===")

# Import entire modules
import math
import random
from datetime import datetime

# Using math module
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi:.4f}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")

# Using random module
print(f"Random number (1-10): {random.randint(1, 10)}")
colors = ["red", "blue", "green", "yellow"]
print(f"Random color: {random.choice(colors)}")

# Using datetime
now = datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Import specific functions
from math import factorial, pow

print(f"Factorial of 5: {factorial(5)}")
print(f"2 to the power of 8: {pow(2, 8)}")
print()

# =====================================
# 11. CREATING YOUR OWN MODULE
# =====================================

print("=== CREATING YOUR OWN MODULE ===")

# We'll create a separate file for this
print("See 'my_utilities.py' for an example of creating your own module")
print("Then you can import it with: import my_utilities")
print()

# =====================================
# 12. EXERCISES FOR PRACTICE
# =====================================

print("=== PRACTICE EXERCISES ===")
print("Try these exercises:")
print("1. Write a function that converts temperature from Celsius to Fahrenheit")
print("2. Create a function that finds the largest number in a list")
print("3. Write a function that counts vowels in a string")
print("4. Create a calculator function that takes operation and numbers")
print("5. Write a function that validates if a password is strong")
print()

# Example solutions (uncomment to see):
#
# # Exercise 1: Temperature converter
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# temp_c = 25
# temp_f = celsius_to_fahrenheit(temp_c)
# print(f"{temp_c}°C = {temp_f}°F")
#
# # Exercise 2: Find largest number
# def find_largest(numbers):
#     if not numbers:
#         return None
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest
#
# nums = [3, 7, 2, 9, 1]
# print(f"Largest in {nums}: {find_largest(nums)}")
#
# # Exercise 3: Count vowels
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
#
# word = "Programming"
# print(f"Vowels in '{word}': {count_vowels(word)}")

print("Excellent work completing Lesson 3!")
print("Next up: Lesson 4 - Data Structures")