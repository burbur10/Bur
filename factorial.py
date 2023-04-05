def fact(n):

    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
result = fact(6)
print(result)



import collections

# Define the statement
statement = "The quick brown fox jumps over the lazy dog"

# Remove all spaces and convert to lowercase
statement = statement.replace(" ", "").lower()

# Count the occurrences of each letter
count = collections.Counter(statement)

# Find the most common letter
most_common_letter = max(count, key=count.get)

# Print the most common letter and its count
print(f"The most common letter is '{most_common_letter}' with a count of {count[most_common_letter]}.")