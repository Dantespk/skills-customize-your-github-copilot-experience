# 📘 Assignment: Exception Handling in Python

## 🎯 Objective

Master error handling in Python by learning to write robust, defensive code. You'll learn to catch and handle different types of exceptions, create custom exceptions, and build applications that gracefully handle real-world errors instead of crashing.

## 📝 Tasks

### 🛠️ Task 1: Catch Errors with Try/Except Blocks

#### Description
Learn the basics of exception handling by writing try/except blocks that catch common runtime errors. This task teaches you how to prevent your program from crashing when something goes wrong.

#### Requirements
Completed program should:

- Use try/except blocks to handle at least three different error scenarios
- Catch at least two different built-in exception types (e.g., `ValueError`, `ZeroDivisionError`, `IndexError`)
- Print user-friendly error messages when exceptions occur
- Continue execution after handling an exception (don't let the program crash)
- Test the code with both valid and invalid inputs

### 🛠️ Task 2: Handle Multiple Exception Types

#### Description
Expand your error handling by managing different types of exceptions with specific handlers. This task teaches you how to respond differently depending on what type of error occurred.

#### Requirements
Completed program should:

- Define separate exception handlers for at least three different exception types
- Include a generic exception handler as a fallback
- Use `except` clauses in the correct order (specific exceptions before generic)
- Include an `else` block that runs when no exception occurs
- Include a `finally` block that always executes (e.g., cleanup code)

### 🛠️ Task 3: Create and Raise Custom Exceptions

#### Description
Learn to define your own exception classes to represent specific errors in your application. This task teaches professional error handling patterns used in production code.

#### Requirements
Completed program should:

- Define at least two custom exception classes that inherit from `Exception`
- Raise custom exceptions when validation fails or invalid operations occur
- Include meaningful error messages in your custom exceptions
- Catch and handle your custom exceptions with specific handlers
- Demonstrate the difference between built-in and custom exceptions

### 🛠️ Task 4: Build a Robust File Processor (Stretch Goal)

#### Description
Combine all exception handling skills to build a real-world application that safely processes user input and file operations. This task demonstrates how error handling protects your application in production scenarios.

#### Requirements
Completed program should:

- Read data from a file (handle file not found, permission errors)
- Parse the file content (handle format/parsing errors)
- Validate the data before processing (use custom exceptions)
- Handle invalid user input gracefully (use try/except)
- Provide informative error messages that help users understand what went wrong
- Use a `finally` block to ensure resources are properly closed
- Continue processing valid records even when some records fail
