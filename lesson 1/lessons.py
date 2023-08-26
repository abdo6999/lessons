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




# Lesson 3: Basic Input and Output
# - Learn how to take user input and display output using print().

# Lesson 4: Conditional Statements
# - Explore if, elif, and else statements for decision-making.

# Lesson 5: Loops
# - Learn about for and while loops for repetitive tasks.

# Lesson 6: Lists and Tuples
# - Understand how to create, access, and modify lists and tuples.

# Lesson 7: Dictionaries and Sets
# - Explore dictionaries and sets for storing key-value pairs and unique values.

# Lesson 8: Functions
# - Define and use functions to organize your code.

# Lesson 9: Modules and Libraries
# - Learn how to import and use external modules and libraries.

# Lesson 10: File Handling
# - Read and write data to files using Python.

# Lesson 11: Exception Handling
# - Understand how to handle errors and exceptions gracefully.

# Lesson 12: Object-Oriented Programming (OOP)
# - Learn the basics of classes and objects.

# Lesson 13: Advanced Topics (Choose one or more depending on your interests):
#   - Regular Expressions
#   - Working with APIs
#   - Web Scraping
#   - Data Analysis with Pandas
#   - GUI Development (e.g., Tkinter)

# Lesson 14: Final Projects
# - Apply your knowledge to create small projects or scripts.

# Lesson 15: Additional Resources and Practice
# - Explore online tutorials, exercises, and coding challenges to further improve your skills.
