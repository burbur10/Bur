def filter_strings(strings):
    word = []
    for string in strings:
        if string.startswith('a'):
          word.append(string)
    return word

strings = ["apple", "apricot", "mango", "orange"]
word  = filter_strings(strings)
print(word)