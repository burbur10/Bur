numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# use a lambda function to filter out the odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Original list: ", numbers)
print("Odd numbers: ", odd_numbers)