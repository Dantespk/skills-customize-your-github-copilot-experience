# Exception Handling in Python - Starter Code

# Task 1: Basic Try/Except Practice
print("=== Task 1: Basic Try/Except ===")
# TODO: Write try/except blocks to handle:
#   - ZeroDivisionError (divide by zero)
#   - ValueError (invalid input conversion)
#   - IndexError (accessing invalid list index)


# Task 2: Multiple Exception Types
print("\n=== Task 2: Multiple Exception Types ===")
# TODO: Create a function that:
#   - Opens and reads a file
#   - Uses separate exception handlers for FileNotFoundError, IOError, and generic Exception
#   - Includes an else block
#   - Includes a finally block


# Task 3: Custom Exceptions
print("\n=== Task 3: Custom Exceptions ===")
# TODO: Define custom exception classes:
#   - InvalidAgeError (for age validation)
#   - InvalidEmailError (for email validation)
# TODO: Create validation functions that raise these exceptions
# TODO: Handle the custom exceptions appropriately


# Task 4: Robust File Processor (Stretch Goal)
print("\n=== Task 4: File Processor ===")
# TODO: Build a file processor that:
#   - Reads data from a CSV file (handle FileNotFoundError)
#   - Parses each line (handle malformed data)
#   - Validates records using custom exceptions
#   - Continues processing valid records even if some fail
#   - Reports detailed errors for each failure
