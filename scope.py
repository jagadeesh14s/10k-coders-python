 Global scope: x and y are defined here
x = 5
y = 10

def calculate_sum():
    """Calculate the sum of global variables x and y using a local variable z."""
    # Local scope: z is defined inside the function
    z = x + y
    return z

# Execute the function and print the result
result = calculate_sum()
print("Sum of x and y is:", result)

output:
Sum of x and y is: 15
