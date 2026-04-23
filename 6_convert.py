#type conversion in python
a = 5
b = 10.5
print(type(a)) #output will be <class 'int'> because a is an integer
print(type(b)) #output will be <class 'float'> because b is a float

#converting integer to float
c = float(a)
print(c) #output will be 5.0 because we have converted integer a to float
print(type(c)) #output will be <class 'float'> because c is now a float

print(str(b)) #output will be '10.5' because we have converted float b to string
print(type(str(b))) #output will be <class 'str'> because str(b) is now a string