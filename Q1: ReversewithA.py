import sys

phrase = str(input("Enter phrase or string to use: "))
insert_var = str(input("Enter variable to add: "))

# Function to reverse
def rev_fuction(x):
    return x[::-1]  # Return last char first


rev_phrase = rev_fuction(phrase)  # Reverse phrase
rev_phrase = rev_phrase.split(" ")  # Split strings into list
phrase_A = 'A'.join(rev_phrase)  # Join string with A in between


new_A_phrase = phrase_A.split(" ")  # Split into list

new_A_phrase.insert(0, insert_var)  # Add "A" in the front
new_A_phrase.append(insert_var)  # Add "A" at the end
final_phrase = ''.join(new_A_phrase)  # Join everything together

print(final_phrase)  # Print result

