# Strings in Python
a = "Hello, World!"
print(a)

#string functions
print(len(a)) # length of the string
print(a.upper()) # convert to uppercase
print(a.lower()) # convert to lowercase
print(a.replace("H", "J")) # replace H with J
print(a.index("l")) # find the index of the first occurrence of l
#strings are immutable, so we cannot change them directly.

b = "guys"

# concatenation
c = a + " " + b
print(c)

#concatenation for numbers
d = 45
e = 55
print(str(d) + str(e)) # we need to convert numbers to strings before concatenation

#Write a python program to display a user entered name followed by Good Afternoon using input () function
name = input("Enter your name: ")
print("Good Afternoon, " + name + "!")

#Write a program to detect double space in a string.
text = "This  is a test string"
position = text.find("  ")
print(position)

#usage of escape sequence characters
print("Hello\nWorld") # new line

#Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\n\tThis Python Course is nice.\nThanks!"
print(letter)