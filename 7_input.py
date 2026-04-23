#input in python

name = (input("Enter your name: ")) #input function takes input from the user and returns it as a string
print("Hello, " + name + "!") #output will be Hello, name

#Write a python program to add two numbers.
a= int(input("enter 1st number:"))
b= int(input("enter 2nd number:"))
print("The sum of", a, "and", b, "is", a+b) #output will be The sum of <a> and <b> is a+b

# Check the type of variable assigned using input () function
c = input("Enter a value: ")
print("The type of variable c is:", type(c)) #it will always return <class 'str'> because input() function returns a string by default, even if you enter a number.

#Write a python program to find an average of two numbers entered by the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The average of", num1, "and", num2, "is", (num1 + num2) / 2) #output will be The average of num1 and num2 is average.

#Write a python program to calculate the square of a number entered by the user.
num = int(input("Enter a number: "))
print("The square of", num, "is", num ** 2) #output will be The square of num is num**2
