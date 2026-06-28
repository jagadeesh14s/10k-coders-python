# List comprehension: generate squares of numbers from 1 to 10
list_of_squares = [num ** 2 for num in range(1, 11)]
print("List of squares:", list_of_squares)

output:
List of squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Set comprehension: create a set of unique squares
set_of_squares = {num ** 2 for num in range(1, 11)}
print("Set of unique squares:", set_of_squares)

output:
Set of unique squares: {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

# Dictionary comprehension: number as key, square as value
dict_of_squares = {num: num ** 2 for num in range(1, 11)}
print("Dictionary of squares:", dict_of_squares)

output:
Dictionary of squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
