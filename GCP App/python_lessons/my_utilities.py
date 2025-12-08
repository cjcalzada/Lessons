# my_utilities.py - A custom module for demonstration
"""
This is a custom utility module that demonstrates how to create
your own Python module with useful functions.
"""

def calculate_area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_area_circle(radius):
    """Calculate the area of a circle."""
    import math
    return math.pi * radius ** 2

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def capitalize_words(text):
    """Capitalize each word in a string."""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

# Module constants
PI = 3.14159
GREETING = "Hello from my_utilities module!"

# This code runs when the module is imported
print("my_utilities module loaded successfully!")

# This code only runs when the file is executed directly
if __name__ == "__main__":
    print("Testing my_utilities module...")
    print(f"Area of rectangle (5x3): {calculate_area_rectangle(5, 3)}")
    print(f"Area of circle (r=4): {calculate_area_circle(4):.2f}")
    print(f"Is 10 even? {is_even(10)}")
    print(f"Capitalized 'hello world': {capitalize_words('hello world')}")
    print(f"Reversed 'Python': {reverse_string('Python')}")