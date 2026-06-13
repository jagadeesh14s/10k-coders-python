# 1.Create a Python function to generate and print a pyramid pattern of asterisks "(*)" with a user-provided height, ensuring the base of the pyramid has a width equal to the height.
def pyramid(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars  = "* " * i
        print(spaces + stars)
height=int(input("Enter the height of the pyramid: "))
pyramid(height)

output:
Enter the height of the pyramid: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

#2.Develop a Python program to recognize and count the occurrences of a specific sequence pattern (e.g., "abc") within a given string.
def count_pattern(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count
text = "abcxyzabcrgabc"
pattern = "abc"
print("Occurrences:", count_pattern(text, pattern))

output:
Occurrences: 3

#3.Write a Python script to generate and display a checkerboard pattern of a specified size, using alternating 'X' and 'O' characters for the squares.
def checkerboard(size):
    for i in range(size):
        res = ""
        for j in range(size):
            if (i + j) % 2 == 0:
                res += "X "
            else:
                res += "O "
        print(res)
checkerboard(5)

output:
X O X O X
O X O X O 
X O X O X
O X O X O
X O X O X 
