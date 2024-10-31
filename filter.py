# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to get only even numbers
even_numbers = list(filter(is_even, numbers))

print("Even numbers:", even_numbers)
