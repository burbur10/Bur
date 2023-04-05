def remove_vowels(word):
    
    for q in word:
        if q in "aeiou":
          word.remove(q)
        print(word)
word = input("Enter a word: ")
