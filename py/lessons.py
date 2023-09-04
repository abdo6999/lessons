# Lesson 1: Introduction to Python
# - Learn what Python is and why it's popular.
# - Install Python and a code editor if you haven't already.
# python is a interpreter multithreaded languish famous for minimum syntax



# Lesson 2: Variables and Data Types
# - Understand how to declare variables.
# - Explore data types like int, float, str, and bool.















# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================






#  Data Types in Programming
# - Data types are a fundamental concept in programming.
# - They define the kind of data that can be stored and manipulated in a program.
# - Data types provide information about:
#   - What operations can be performed on the data.
#   - How much memory the data occupies.

#  Data Size
# - Data size refers to the amount of memory required to store a value of a specific data type.
# - In programming, data size is typically measured in bits or bytes.
# - Smaller data types use less memory, while larger data types consume more.

# Constants for data sizes
BIT = 1   #  value of 0 or 1.
BYTE = 8 * BIT        # ex: a = "01100001"
KILOBYTE = 1024 * BYTE   # Equals 1,024 bytes (2^10), often used to measure the size of small text files or images.
MEGABYTE = 1024 * KILOBYTE   # Equals 1,024 kilobytes (2^20), used for larger files, such as high-resolution images or short videos.
GIGABYTE = 1024 * MEGABYTE   # Equals 1,024 megabytes (2^30), frequently used to measure the size of files, programs, and data storage.


# Common Data Types and Their Approximate Sizes:
# - bool: 1 byte (8 bits) - Represents true or false.
# - char: 1 byte (8 bits) - Represents a single character.
# - int: 4 bytes (32 bits) - Represents integers.
# - float: 4 bytes (32 bits) - Represents single-precision floating-point numbers.
# - double: 8 bytes (64 bits) - Represents double-precision floating-point numbers.
# - str: Variable size - Represents sequences of characters (size depends on the string length).
# - list or array: Variable size - Represents ordered collections of data.
# - dict or map: Variable size - Represents key-value pairs.
# - set: Variable size - Represents a collection of unique elements.

# Understanding data sizes is important for optimizing memory usage in programs.
# Choosing the appropriate data type for a variable helps minimize memory waste and enhances performance.

# Example:
# An integer variable in Python (int) typically consumes 4 bytes (32 bits) of memory.
# This means it can represent values from -2,147,483,648 to 2,147,483,647.

#  Dynamic Typing and Memory Management
# - Dynamic typing in languages like Python allows for flexibility but may consume more memory.
# - Some languages like C++ offer more precise control over memory allocation.







# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================
# =================================================================================================================























# In Python, variables are used to store data. You can think of them as containers
# that hold different types of information. Python has several built-in data types.

# 2.1 Variable Declaration
# - Variables are declared by assigning a value to a name.
# - Variable names can contain letters, numbers, and underscores but can't start with a number.
# - They are case-sensitive, so 'myVariable' and 'myvariable' are different.

# Example:
my_variable = 42
name = "John"
is_valid = True
pi = 3.14159

# 2.2 Numeric Data Types
# - Integers (int): Whole numbers without a decimal point.
# - Floating-point numbers (float): Numbers with a decimal point.
# - Python automatically converts between these types as needed.

# Example:
integer_number = 42
floating_point_number = 3.14159

# 2.3 Text Data Type
# - Strings (str): Used to represent text.
# - Enclose strings in single (' ') or double (" ") quotes.

# Example:
name = "Alice"
greeting = 'Hello, World!'

# 2.4 Boolean Data Type
# - Booleans (bool): Represents True or False values, often used for decision making.
# - Result of comparisons and logical operations.

# Example:
is_valid = True
is_error = False

# 2.5 Dynamic Typing
# - Python is dynamically typed, which means you don't need to declare a variable's type.
# - The interpreter infers the type based on the assigned value.

# Example:
dynamic_variable = 42
dynamic_variable = "Hello"

# 2.6 Type Conversion
# - You can convert between data types using functions like int(), float(), and str().

# Example:
age = "25"
age_integer = int(age)

# 2.7 Variable Naming Best Practices
# - Use meaningful variable names to make your code more readable.
# - Follow a consistent naming convention (e.g., snake_case or CamelCase).
# - Avoid using reserved words (e.g., 'if', 'while') as variable names.

# Example:
user_age = 25
user_name = "Alice"

# 2.8 Comments
# - Use comments (lines starting with #) to add explanations to your code.

# Example:
# Calculate the sum of two numbers
result = 10 + 5

# 2.9 Exercise
# - Create variables of different data types.
# - Perform basic operations on them (e.g., addition, subtraction, concatenation).

# Example:
# Calculate the area of a rectangle
length = 5
width = 3
area = length * width

# 2.10 Summary
# - Variables store data.
# - Python has int, float, str, and bool data types.
# - Variables are dynamically typed.
# - Use meaningful names and comments to make your code readable.




# Lesson 3: Input and Output

# Input
# - Taking user input using the input() function.
# - The input() function reads a line of text from the user and returns it as a string.

user_input = input("Enter your name: ")  # Prompt the user for their name
print("Hello, " + user_input + "!")     # Display a greeting with the user's name

# Output
# - Displaying information to the user using the print() function.
# - The print() function is used to output text or variables to the console.

print("This is a simple Python program.")  # Display a message to the user
result = 10 + 5
print("The result of 10 + 5 is:", result)   # Display the result of an arithmetic operation

# Combining Input and Output
# - Taking user input and using it in the program's output.

age = input("Enter your age: ")  # Prompt the user for their age
age = int(age)  # Convert the user's input to an integer
future_age = age + 10
print("In 10 years, you will be", future_age, "years old.")

# Summary
# - Input is obtained using the input() function.
# - Output is displayed using the print() function.
# - You can combine input and output to create interactive programs.

# Now, you have a basic understanding of how to get input from users and display output in Python.
# Lesson: Printing and Taking Input in Python

# Printing in Python with `print()`

# Basic Usage:
print("Hello, World!")  # Outputs the text "Hello, World!"

# Separating Items:
print(1, 2, 3)  # Outputs: 1 2 3

# Customize the separator using the `sep` parameter:
print(1, 2, 3, sep='-')  # Outputs: 1-2-3

# Controlling the End Character:
# The `end` parameter specifies what to print at the end (default is newline '\n'):
print("Hello", end=' ')
print("World!")  # Outputs: Hello World!

# Formatting Output:

name = "Alice"
age = 30

# Using placeholders with `.format()`:
print("My name is {} and I am {} years old.".format(name, age))

# Old Style Formatting (%):
print("My name is %s and I am %d years old." % (name, age))

# F-strings (Python 3.6+):
print(f"My name is {name} and I am {age} years old.")

# Taking Input with `input()`

# The `input()` function allows getting user input:
name = input("Enter your name: ")
print("Hello, " + name + "!")

# By default, `input()` treats input as a string.
# If you need a numeric value, convert it using `int()` or `float()`:
age = int(input("Enter your age: "))

# Remember to handle potential errors when converting input to numbers.
# Python's simplicity and flexibility make it an excellent choice for both beginners and experienced developers.


# Coding Challenge: User Info

# Lesson 1: Introduction to Python
# Create a program that welcomes the user and explains what this program does.

print("Welcome to the User Info program!")
print("This program will collect some information about you.")

# Lesson 2: Variables and Data Types
# Ask the user for their name, age, and favorite color, and store this information in variables.

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to an integer
favorite_color = input("Enter your favorite color: ")

# Lesson 3: Input and Output
# Display the collected information in a nicely formatted message.

print("\nHere's the information you provided:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Color: {favorite_color}")

# Coding Challenge: Modify the program
# Now, modify the program to calculate and display the user's birth year based on their age.

birth_year = 2023 - age
print(f"\nBased on your age, your birth year is approximately {birth_year}.")

# Challenge: Improve the program
# Add error handling to handle invalid age inputs (e.g., non-numeric values).

# Hint: You can use a try-except block to catch potential ValueError exceptions when converting age to an integer.
try:
    age = int(input("Enter your age: "))
    birth_year = 2023 - age
    print(f"\nBased on your age, your birth year is approximately {birth_year}.")
except ValueError:
    print("Invalid age input. Please enter a valid numeric age.")

# Challenge: Personalize the program further by adding more questions or customizing the output messages.

# You can ask additional questions and display the user's input in a creative way.

# Enjoy coding and personalizing your user info program!

# الدرس 4: الدوال والأساليب المدمجة لأنواع البيانات


# جزء 1: أنواع البيانات العددية

# 1.1 abs()
# تقوم الدالة abs() بإعادة القيمة المطلقة لرقم. يتم التعامل مع القيمة دون الاهتمام بالعلامة.

num = -5
absolute_value = abs(num)  # سيكون القيمة المطلقة هي 5

# 1.2 round()
# تقوم الدالة round() بتقريب رقم إلى الأقرب. يمكن تحديد عدد الأماكن العشرية.

number = 3.14159
rounded = round(number, 2)  # سيكون الرقم المقرب بـ 2 أماكن عشرية هو 3.14

# 1.3 max() و min()
# تقوم الدوال max() و min() بإيجاد القيمة الكبرى والصغرى في مجموعة من الأرقام.

numbers = [5, 2, 9, 1, 7]
maximum = max(numbers)  # سيكون القيمة الكبرى هي 9
minimum = min(numbers)  # سيكون القيمة الصغرى هي 1

# 1.4 sum()
# تقوم الدالة sum() بجمع جميع الأرقام في مجموعة.

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # سيكون المجموع هو 15

# 1.5 pow()
# تقوم الدالة pow() برفع رقم إلى قوة أخرى.

base = 2
exponent = 3
result = pow(base, exponent)  # سيكون الناتج هو 2^3 = 8

# 1.6 divmod()
# تقوم الدالة divmod() بالقسمة وإعادة القسمة والباقي.

quotient, remainder = divmod(10, 3)  # سيكون الناتج: النصفين 3 والباقي 1

# 1.7 int() و float()
# تقوم الدوال int() و float() بتحويل الأنواع بين الأعداد الصحيحة والأعداد العشرية.

integer_number = int(5.7)  # سيتم تحويل 5.7 إلى 5
float_number = float(42)   # سيتم تحويل 42 إلى 42.0

# 1.8 complex()
# تقوم الدالة complex() بإنشاء أعداد مركبة (أعداد خيالية).

complex_number = complex(3, 4)  # سيكون الرقم المركب هو 3 + 4j


# Lesson 5: Conditional Statements
# - Explore if, elif, and else statements for decision-making.

# Lesson 6: Loops
# - Learn about for and while loops for repetitive tasks.

# Lesson 7: Lists and Tuples
# - Understand how to create, access, and modify lists and tuples.

# Lesson 8: Dictionaries and Sets
# - Explore dictionaries and sets for storing key-value pairs and unique values.

# Lesson 9: Functions
# - Define and use functions to organize your code.

# Lesson 10: Modules and Libraries
# - Learn how to import and use external modules and libraries.

# Lesson 11: File Handling
# - Read and write data to files using Python.

# Lesson 12: Exception Handling
# - Understand how to handle errors and exceptions gracefully.

# Lesson 13: Object-Oriented Programming (OOP)
# - Learn the basics of classes and objects.

# Lesson 14: Advanced Topics (Choose one or more depending on your interests):
#   - Regular Expressions
#   - Working with APIs
#   - Web Scraping
#   - Data Analysis with Pandas
#   - GUI Development (e.g., Tkinter)

# Lesson 15: Final Projects
# - Apply your knowledge to create small projects or scripts.

# Lesson 16: Additional Resources and Practice
# - Explore online tutorials, exercises, and coding challenges to further improve your skills.
