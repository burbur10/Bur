def number_of_vowels(word):
    #assume the initial number of vowels is zero
    number = 0
    for letter in word:
        if letter in "aeiou":
            number +=1
    return number
word = input("Enter a word: ")
no_of_vowels = number_of_vowels(word)
print("The number of vowels are: " + str(no_of_vowels))