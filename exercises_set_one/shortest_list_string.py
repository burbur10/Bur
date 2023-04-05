def shortest_string(strings):
    shortest = strings[0]
    for string in strings:
        if len(string) < len(shortest):
            shortest = string
    return string


strings = [input("Enter a word: "), input("Enter another word: "), input("Enter a third word: ")]
shorter = shortest_string(strings)
print("The shortest word is: " + shorter)