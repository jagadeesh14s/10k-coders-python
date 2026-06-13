#Generate a pyramid pattern of a specified height using asterisks (*), where the base of the pyramid is aligned with the left margin.
rows=5
for row in range(rows):
    res=" "
    for col in range(row+1):
        res+="*"+" "
    print(res)

output:
 * 
 * * 
 * * * 
 * * * * 
 * * * * * 

#Create a function to print a square pattern of a given size filled with a specified character.
rows=5
for i in range(rows):
    res=" "
    for j in range(rows):
        res+="*"+" "
    print(res)

output:
 * * * * * 
 * * * * * 
 * * * * * 
 * * * * * 
 * * * * * 

#Develop a program to display a diamond pattern of asterisks (*) with a specified width, ensuring symmetry and proper alignment.
rows=5
for i in range(1,rows+1):
    res=""
    for sp in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="* "
    print(res)

for i in range(rows-1,0,-1):
    res=""
    for sp in range(rows-i):
        res+=" "
    for j in range(i):
        res+="* "
    print(res) 

output:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
