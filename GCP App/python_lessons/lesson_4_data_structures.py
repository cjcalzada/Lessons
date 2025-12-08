# Lesson 4: Data Structures
# This file covers lists, dictionaries, tuples, sets, and working with collections

print("=== LESSON 4: DATA STRUCTURES ===")
print("Learning to work with different ways to store and organize data")
print()

# =====================================
# 1. LISTS - ORDERED, MUTABLE COLLECTIONS
# =====================================

print("=== LISTS ===")

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty_list = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Empty list: {empty_list}")

# Accessing list elements (indexing starts at 0)
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")  # Negative indexing
print(f"Second and third fruits: {fruits[1:3]}")  # Slicing
print()

# Modifying lists
fruits.append("grape")  # Add to end
fruits.insert(1, "strawberry")  # Insert at position
fruits.remove("banana")  # Remove specific item
popped = fruits.pop()  # Remove and return last item

print(f"After modifications: {fruits}")
print(f"Popped item: {popped}")
print()

# List methods and operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of 1's: {numbers.count(1)}")
print(f"Index of first 4: {numbers.index(4)}")

numbers.sort()  # Sort in place
print(f"Sorted: {numbers}")

numbers.reverse()  # Reverse in place
print(f"Reversed: {numbers}")

# List comprehensions (advanced list creation)
squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Squares of 1-5: {squares}")
print(f"Even numbers 1-10: {even_numbers}")
print()

# =====================================
# 2. DICTIONARIES - KEY-VALUE PAIRS
# =====================================

print("=== DICTIONARIES ===")

# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Alternative way to create
colors = dict(red="#FF0000", green="#00FF00", blue="#0000FF")

print(f"Student: {student}")
print(f"Colors: {colors}")

# Accessing dictionary values
print(f"Student name: {student['name']}")
print(f"Student GPA: {student.get('gpa')}")
print(f"Student year: {student.get('year', 'Not specified')}")  # Default value

# Modifying dictionaries
student["age"] = 21  # Update existing key
student["email"] = "alice@example.com"  # Add new key
del student["major"]  # Remove key

print(f"Modified student: {student}")
print()

# Dictionary methods
print("Dictionary keys:", list(student.keys()))
print("Dictionary values:", list(student.values()))
print("Dictionary items:", list(student.items()))

# Looping through dictionaries
print("\nStudent information:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

# Nested dictionaries
school = {
    "name": "Tech University",
    "students": {
        "alice": {"age": 20, "major": "CS"},
        "bob": {"age": 22, "major": "Math"}
    },
    "courses": ["Python", "Calculus", "Physics"]
}

print(f"School: {school['name']}")
print(f"Alice's major: {school['students']['alice']['major']}")
print()

# =====================================
# 3. TUPLES - ORDERED, IMMUTABLE COLLECTIONS
# =====================================

print("=== TUPLES ===")

# Creating tuples
coordinates = (3, 4)
person = ("John", "Doe", 30, "Engineer")
single_item = (42,)  # Note the comma for single-item tuple
empty_tuple = ()

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Single item: {single_item}")

# Accessing tuple elements (same as lists)
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"First name: {person[0]}")

# Tuple unpacking
x, y = coordinates
first_name, last_name, age, job = person
print(f"Unpacked coordinates: x={x}, y={y}")
print(f"Unpacked person: {first_name} {last_name}, {age}, {job}")

# Tuples are immutable (cannot be changed)
# coordinates[0] = 5  # This would cause an error!

# But you can create new tuples
new_coordinates = (5, 6)
print(f"New coordinates: {new_coordinates}")
print()

# =====================================
# 4. SETS - UNORDERED, UNIQUE COLLECTIONS
# =====================================

print("=== SETS ===")

# Creating sets
fruits_set = {"apple", "banana", "orange"}
numbers_set = {1, 2, 3, 4, 5}
mixed_set = {"hello", 42, 3.14}

print(f"Fruits set: {fruits_set}")
print(f"Numbers set: {numbers_set}")

# Sets automatically remove duplicates
duplicate_numbers = {1, 2, 2, 3, 3, 3, 4}
print(f"Duplicates removed: {duplicate_numbers}")

# Adding and removing from sets
fruits_set.add("grape")
fruits_set.add("apple")  # Won't add duplicate
fruits_set.discard("banana")  # Remove if present
print(f"Modified fruits set: {fruits_set}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union (all items): {set1.union(set2)}")
print(f"Intersection (common items): {set1.intersection(set2)}")
print(f"Difference (in set1 but not set2): {set1.difference(set2)}")
print()

# =====================================
# 5. WORKING WITH COLLECTIONS
# =====================================

print("=== WORKING WITH COLLECTIONS ===")

# Converting between types
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers_list)
numbers_set = set(numbers_list)

print(f"List: {numbers_list}")
print(f"Tuple: {numbers_tuple}")
print(f"Set: {numbers_set}")

# Finding items in collections
print(f"3 in list: {3 in numbers_list}")
print(f"6 in set: {6 in numbers_set}")

# Checking if key exists in dictionary
student = {"name": "Alice", "age": 20}
print(f"'name' in dictionary: {'name' in student}")
print(f"'grade' in dictionary: {'grade' in student}")
print()

# =====================================
# 6. PRACTICAL EXAMPLES
# =====================================

print("=== PRACTICAL EXAMPLES ===")

# Example 1: Managing a to-do list
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added: {task}")

def complete_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Completed: {task}")
    else:
        print(f"Task not found: {task}")

def show_tasks():
    if todo_list:
        print("To-do list:")
        for i, task in enumerate(todo_list, 1):
            print(f"  {i}. {task}")
    else:
        print("No tasks!")

add_task("Learn Python")
add_task("Write code")
add_task("Practice exercises")
show_tasks()
complete_task("Learn Python")
show_tasks()
print()

# Example 2: Word frequency counter
text = "the quick brown fox jumps over the lazy dog the fox is quick"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")
print()

# Example 3: Contact book
contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}

def get_contact(name):
    return contacts.get(name, "Contact not found")

def list_contacts():
    if contacts:
        print("Contact book:")
        for name, info in contacts.items():
            print(f"  {name}: {info['phone']}, {info['email']}")
    else:
        print("No contacts")

add_contact("Alice", "123-456-7890", "alice@email.com")
add_contact("Bob", "987-654-3210", "bob@email.com")
list_contacts()
print(f"Alice's info: {get_contact('Alice')}")
print()

# Example 4: Set operations for data analysis
students_math = {"Alice", "Bob", "Charlie", "Diana"}
students_science = {"Bob", "Charlie", "Eve", "Frank"}

print(f"Math students: {students_math}")
print(f"Science students: {students_science}")
print(f"Both subjects: {students_math.intersection(students_science)}")
print(f"Only math: {students_math.difference(students_science)}")
print(f"Only science: {students_science.difference(students_math)}")
print(f"All students: {students_math.union(students_science)}")
print()

# =====================================
# 7. CHOOSING THE RIGHT DATA STRUCTURE
# =====================================

print("=== CHOOSING THE RIGHT DATA STRUCTURE ===")
print("When to use each type:")
print("LIST: When you need ordered, changeable collections")
print("      - Shopping lists, scores, sequences")
print("DICT: When you need key-value relationships")
print("      - User profiles, configurations, mappings")
print("TUPLE: When you need ordered, unchangeable collections")
print("       - Coordinates, RGB colors, database records")
print("SET: When you need unique items or set operations")
print("     - Tags, unique IDs, removing duplicates")
print()

# =====================================
# 8. EXERCISES FOR PRACTICE
# =====================================

print("=== PRACTICE EXERCISES ===")
print("Try these exercises:")
print("1. Create a grocery list and practice adding/removing items")
print("2. Build a simple phone book using a dictionary")
print("3. Find common elements between two lists using sets")
print("4. Create a student grade tracker with lists and dictionaries")
print("5. Write a function to remove duplicates from a list")
print()

# Example solutions (uncomment to see):
#
# # Exercise 1: Grocery list
# grocery_list = ["milk", "eggs", "bread"]
# grocery_list.append("cheese")
# grocery_list.remove("eggs")
# print(f"Grocery list: {grocery_list}")
#
# # Exercise 2: Phone book
# phone_book = {
#     "Alice": "123-456-7890",
#     "Bob": "987-654-3210"
# }
# phone_book["Charlie"] = "555-123-4567"
# print(f"Alice's number: {phone_book.get('Alice')}")
#
# # Exercise 3: Common elements
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common = list(set(list1).intersection(set(list2)))
# print(f"Common elements: {common}")
#
# # Exercise 5: Remove duplicates
# def remove_duplicates(items):
#     return list(set(items))
#
# numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4]
# unique_numbers = remove_duplicates(numbers_with_dupes)
# print(f"Original: {numbers_with_dupes}")
# print(f"Unique: {unique_numbers}")

print("Fantastic! You've completed Lesson 4!")
print("Next: Advanced topics and real-world projects")