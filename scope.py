# Global scope: x and y are defined here
x = 5
y = 10

def calculate_sum():
    """Calculate the sum of global variables x and y using a local variable z."""
    z = x + y
    return z

result = calculate_sum()
print("Sum of x and y is:", result)

output:
Sum of x and y is: 15
