# a. Create a list of squares for the numbers from 1 to 5 using list comprehension.

#sqaures = [ i**2 for i in range(1, 6)]

squares = []

for i in range(1, 6):
    squares.append(i**2)

print(squares)

# b. Create a list of even numbers from 2 to 10 using list comprehension.
even = []

for x in range(2, 11, 2):
    even.append(x)

print(even)

# c. Create a list of names in uppercase from the list of people in Exercise 3.
people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]

NAMES = []

for i in people:
    NAME = i["name"].upper()
    NAMES.append(NAME)

print(NAMES)