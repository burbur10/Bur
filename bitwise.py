
def are_anagrams(word1, word2):
    # Convert both words to lowercase and remove spaces/punctuation
    word1 = ''.join(filter(str.isalpha, word1.lower()))
    word2 = ''.join(filter(str.isalpha, word2.lower()))

    # Sort the letters in each word
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    # Compare the sorted letters
    return sorted_word1 == sorted_word2

(word1, word2) = input("Enter a word: ", "Enter a word: ")