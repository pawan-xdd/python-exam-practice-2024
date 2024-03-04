# Define a custom exception class
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Function that raises the custom exception
def check_value(x):
    if x < 0:
        raise MyCustomException("Value cannot be negative!")

# Example usage
try:
    value = int(input("Enter a positive number: "))
    check_value(value)
    print("The number entered is:", value)
except ValueError:
    print("Please enter a valid integer.")
except MyCustomException as e:
    print("Custom Exception:", e)
