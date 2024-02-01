# a. Create a list of dictionaries, where each dictionary represents a person.
people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]

# b. Print the name of the second person in the list.
print(people[1]["name"])

# c. Update the age of the third person to 30.
people[2]["age"] = 30

# d. Add a new person to the list.
new_person = {
    "name": "Breanna",
    "age": 20,
    "city": "Kingston"
}

people.append(new_person)

# e. Print the list after the modifications.
print(people)