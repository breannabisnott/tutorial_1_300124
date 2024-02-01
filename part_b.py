# a. Create a list of numbers from 1 to 5.
numbers = [1, 2, 3 , 4 ,5]

# b. Append the number 6 to the list.
numbers.append(6)

# c. Insert the number 0 at the beginning of the list.
numbers = [0] + numbers

# d. Remove the number 3 from the list.
numbers.remove(3)

# e. Print the modified list.
print(numbers)

# f. Check if the number 5 is in the list and print the result.
check = 0

for i in numbers:
    if i == 5:
        check = 1
        
if check == 1:
    print("5 is in the list")
else:
    print("5 is not in the list")