numbers = []

for i in range(1, 11):
    numbers.append(i)

print("After append:", numbers)

numbers.insert(0, 0)
print("After insert:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

last_number = numbers.pop()
print("After pop, last_number =", last_number)
print("List now:", numbers)

position = numbers.index(5)
print("Index of 5:", position)

numbers.clear()
print("After clear:", numbers)
print("Length of list:", len(numbers))

Output:
After append: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After insert: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After sort: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After reverse: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
After pop, last_number = 0
List now: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Index of 5: 5
After clear: []
Length of list: 0
