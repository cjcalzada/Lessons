# Python Practice Exercises
# Test your knowledge with these hands-on exercises!

print("=== PYTHON PRACTICE EXERCISES ===")
print("Work through these exercises to practice what you've learned!")
print()

# =====================================
# EXERCISE 1: CALCULATOR
# =====================================

print("=== EXERCISE 1: SIMPLE CALCULATOR ===")
print("Create a calculator that can add, subtract, multiply, and divide")
print()

def calculator(num1, num2, operation):
    """
    A simple calculator function.
    
    Args:
        num1 (float): First number
        num2 (float): Second number  
        operation (str): '+', '-', '*', or '/'
    
    Returns:
        float: Result of the operation
    """
    # TODO: Complete this function
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero!"
    else:
        return "Error: Invalid operation!"

# Test the calculator
print("Testing calculator:")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
print()

# =====================================
# EXERCISE 2: TEMPERATURE CONVERTER
# =====================================

print("=== EXERCISE 2: TEMPERATURE CONVERTER ===")
print("Convert between Celsius and Fahrenheit")
print()

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # TODO: Implement the conversion formula
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # TODO: Implement the conversion formula
    return (fahrenheit - 32) * 5/9

# Test the converters
print("Testing temperature converters:")
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"32°F = {fahrenheit_to_celsius(32)}°C")
print(f"212°F = {fahrenheit_to_celsius(212)}°C")
print()

# =====================================
# EXERCISE 3: LIST OPERATIONS
# =====================================

print("=== EXERCISE 3: LIST OPERATIONS ===")
print("Practice working with lists")
print()

def find_largest(numbers):
    """Find the largest number in a list."""
    # TODO: Find and return the largest number
    if not numbers:
        return None
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def remove_duplicates(items):
    """Remove duplicates from a list while preserving order."""
    # TODO: Remove duplicates and return new list
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def count_vowels(text):
    """Count vowels in a string."""
    # TODO: Count and return number of vowels
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test the functions
numbers = [3, 7, 2, 9, 1, 9, 3]
print(f"Numbers: {numbers}")
print(f"Largest: {find_largest(numbers)}")
print(f"Remove duplicates: {remove_duplicates(numbers)}")

text = "Programming is fun!"
print(f"Text: '{text}'")
print(f"Vowel count: {count_vowels(text)}")
print()

# =====================================
# EXERCISE 4: STUDENT GRADE MANAGER
# =====================================

print("=== EXERCISE 4: STUDENT GRADE MANAGER ===")
print("Manage student grades using dictionaries")
print()

# Student grade manager
class GradeManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name):
        """Add a new student."""
        # TODO: Add student to self.students dictionary
        if name not in self.students:
            self.students[name] = []
            print(f"Added student: {name}")
        else:
            print(f"Student {name} already exists")
    
    def add_grade(self, name, grade):
        """Add a grade for a student."""
        # TODO: Add grade to student's list of grades
        if name in self.students:
            self.students[name].append(grade)
            print(f"Added grade {grade} for {name}")
        else:
            print(f"Student {name} not found")
    
    def get_average(self, name):
        """Calculate a student's average grade."""
        # TODO: Calculate and return average
        if name in self.students and self.students[name]:
            grades = self.students[name]
            return sum(grades) / len(grades)
        return None
    
    def get_letter_grade(self, average):
        """Convert numerical average to letter grade."""
        # TODO: Return letter grade based on average
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
    def show_report(self):
        """Show a report for all students."""
        # TODO: Display all students and their grades
        print("Student Grade Report:")
        for name, grades in self.students.items():
            if grades:
                average = self.get_average(name)
                letter = self.get_letter_grade(average)
                print(f"  {name}: {grades} -> Average: {average:.1f} ({letter})")
            else:
                print(f"  {name}: No grades yet")

# Test the grade manager
print("Testing Grade Manager:")
gm = GradeManager()
gm.add_student("Alice")
gm.add_student("Bob")
gm.add_grade("Alice", 85)
gm.add_grade("Alice", 92)
gm.add_grade("Alice", 78)
gm.add_grade("Bob", 95)
gm.add_grade("Bob", 88)
gm.show_report()
print()

# =====================================
# EXERCISE 5: WORD GAME
# =====================================

print("=== EXERCISE 5: WORD GAME ===")
print("Simple word guessing game")
print()

def word_guessing_game():
    """Simple word guessing game simulation."""
    import random
    
    words = ["python", "programming", "computer", "science", "coding"]
    secret_word = random.choice(words)
    
    # TODO: Implement the game logic
    guessed_letters = []
    max_attempts = 6
    attempts = 0
    
    print(f"Welcome to Word Guessing Game!")
    print(f"The word has {len(secret_word)} letters")
    
    # Simulate some guesses for demonstration
    simulated_guesses = ['p', 'r', 'o', 'g', 'a', 'm']
    
    for guess in simulated_guesses:
        if attempts >= max_attempts:
            break
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word")
        else:
            attempts += 1
            print(f"Sorry, '{guess}' is not in the word. Attempts left: {max_attempts - attempts}")
        
        # Show current progress
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        print(f"Word: {display}")
        
        # Check if word is complete
        if "_" not in display:
            print("Congratulations! You guessed the word!")
            return
        
        print()
    
    if attempts >= max_attempts:
        print(f"Game over! The word was: {secret_word}")

# Run the word game simulation
word_guessing_game()
print()

# =====================================
# EXERCISE 6: DATA ANALYSIS
# =====================================

print("=== EXERCISE 6: SIMPLE DATA ANALYSIS ===")
print("Analyze some sample data")
print()

# Sample sales data
sales_data = [
    {"date": "2024-01-01", "product": "Laptop", "amount": 999.99, "quantity": 1},
    {"date": "2024-01-01", "product": "Mouse", "amount": 29.99, "quantity": 2},
    {"date": "2024-01-02", "product": "Laptop", "amount": 999.99, "quantity": 1},
    {"date": "2024-01-02", "product": "Keyboard", "amount": 79.99, "quantity": 1},
    {"date": "2024-01-03", "product": "Mouse", "amount": 29.99, "quantity": 3},
]

def analyze_sales(data):
    """Analyze sales data and return summary statistics."""
    # TODO: Calculate various statistics
    
    # Total revenue
    total_revenue = sum(item["amount"] * item["quantity"] for item in data)
    
    # Product counts
    product_counts = {}
    for item in data:
        product = item["product"]
        product_counts[product] = product_counts.get(product, 0) + item["quantity"]
    
    # Best selling product
    best_product = max(product_counts.keys(), key=lambda x: product_counts[x])
    
    # Average transaction amount
    transaction_amounts = [item["amount"] * item["quantity"] for item in data]
    avg_transaction = sum(transaction_amounts) / len(transaction_amounts)
    
    return {
        "total_revenue": total_revenue,
        "product_counts": product_counts,
        "best_product": best_product,
        "average_transaction": avg_transaction,
        "total_transactions": len(data)
    }

# Analyze the sales data
analysis = analyze_sales(sales_data)
print("Sales Analysis Results:")
print(f"Total Revenue: ${analysis['total_revenue']:.2f}")
print(f"Total Transactions: {analysis['total_transactions']}")
print(f"Average Transaction: ${analysis['average_transaction']:.2f}")
print(f"Best Selling Product: {analysis['best_product']}")
print("Product Sales:")
for product, count in analysis['product_counts'].items():
    print(f"  {product}: {count} units")

print()
print("=== CONGRATULATIONS! ===")
print("You've completed the Python practice exercises!")
print("Keep practicing and building projects to improve your skills!")
print()
print("Next steps:")
print("1. Try modifying these exercises")
print("2. Create your own projects")
print("3. Learn about file handling and error handling")
print("4. Explore Python libraries like requests, pandas, matplotlib")
print("5. Build a real application!")