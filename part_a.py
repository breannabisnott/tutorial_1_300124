# Given the following dictionary representing a person:
person = {
    "name": "Alice",
    "age": 28,
    "city": "Wonderland"
}

# a. Print the person's name.
print(person["name"])

# b. Add a new key-value pair to represent the person's occupation (e.g., "engineer").
person["occupation"] = "engineer"

# c. Update the person's age to 29.
person["age"] = 29

# d. Remove the "city" key from the dictionary.
del person["city"]

# e. Print the keys of the modified dictionary.
#print(person.items())
print(person.keys())

#to print keys without dict_keys
person_keys = person.keys()
person_keys_list = list(person_keys)

print(person_keys_list)