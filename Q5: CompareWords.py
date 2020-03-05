import sys

word1 = str(input("Enter full word: "))
word2 = str(input("Enter partial string: "))


def compare_words(w1, w2):
    comp_words = word2 in word1  # Check if the word1 is apart of word2 (case sensitive)
    return comp_words


compResults = compare_words(word1, word2)
binaryVal = int(compResults)  # Convert boolean function to int


print(f"Boolean is {compResults} and Value is equal of  {binaryVal}")
