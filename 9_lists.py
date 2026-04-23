# Lists in Python
L = [1, 2, 3, 4, 5]
A = [ "Pallabi",40, True ,[1,2,3],(1,4,60),{"name":"Pallabi","age":40}] # List can contain different data types
print(L)
print(A)

# List slicing
print(L[0]) # First element
print(L[1:4]) # Elements from index 1 to 3
print(L[-1]) # Last element

# List methods
L.sort() # Sort the list
print(L)

L.append(700) # Append 700 to the list
print(L)

L.pop(2)# Remove and return the last element
print(L) # Remove and return the element at index 5

L.remove(4) # Remove the first occurrence of 4  
print(L) # Print the modified list

L.insert(2, 10) # Insert 10 at index 2
print(L) # Print the modified list

#Write a program to store seven fruits in a list entered by the user.
fruits = []
a1 = (input("Enter the name of fruits you want to store: "))
a2 = (input("Enter the name of fruits you want to store: "))
a3 = (input("Enter the name of fruits you want to store: "))
a4 = (input("Enter the name of fruits you want to store: "))
a5 = (input("Enter the name of fruits you want to store: "))
a6 = (input("Enter the name of fruits you want to store: "))
a7 = (input("Enter the name of fruits you want to store: "))
a8 = (input("Enter the name of fruits you want to store: "))
fruits.append(a1)
fruits.append(a2)
fruits.append(a3)
fruits.append(a4)
fruits.append(a5)
fruits.append(a6)
fruits.append(a7)
fruits.append(a8)
print(fruits)

#Write a program to accept marks of 6 students and display them in a sorted manner

marks = []
m1 = int(input("Enter the marks of student 1: "))
m2 = int(input("Enter the marks of student 2: "))
m3 = int(input("Enter the marks of student 3: "))
m4 = int(input("Enter the marks of student 4: "))
m5 = int(input("Enter the marks of student 5: "))
m6 = int(input("Enter the marks of student 6: "))
marks.append(m1)
marks.append(m2)
marks.append(m3)
marks.append(m4)
marks.append(m5)
marks.append(m6)
marks.sort()
print(marks)

#Write a program to sum a list with 4 numbers.
numbers = []
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
n4 = int(input("Enter a number: "))
numbers.append(n1)
numbers.append(n2)
numbers.append(n3)
numbers.append(n4)
total = sum(numbers)
print("The sum of the numbers is:", total)

