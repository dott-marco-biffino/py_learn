# string manipulation in Python

name = "Dott. Marco Biffino"  # just a simple name

print(name + " is cool")  # + between a couple of strings performs a concatenation

print("Dott.\tMarco\tBiffino")  # '\t' inside a string inserts a tabulation

print("Dott.\nMarco\nBiffino")  # '\n' inside a string inserts a new line

# Don't know what a '\r' does inside a string

print(len(name))

# Case conversion
print(name.upper())  # converts a string to uppercase

print(name.lower())  # converts a string to lowercase

print("questa è una prova".capitalize())  # first character to upper.

print("questa è una prova".swapcase())  # swaps case
print(name.swapcase())

# Substrings

print(name[0])  # extract the first character

print(name[9])  # extract the tenth character

print(name[18])  # extract the last character. A index greater than length(name) is an error

print(name[0:5])

print(name[0:19])

print(name[0:30])

print(name.index("B"))

print(name.replace(__old="Dott.", __new="Altezza Imperiale"))

print("Dott.\tMarco\tBiffinone\tZizzino".expandtabs(tabsize=20))
