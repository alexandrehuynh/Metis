import sys

word1 = "Hello"
word2 = "ello"

def CompareWords(word1, word2):
    comp_words = word2 in word1
    return comp_words


compResults = CompareWords(word1, word2)
binaryVal = int(compResults)


print(f"Boolean is {compResults} and Value is equal of  {binaryVal}")
