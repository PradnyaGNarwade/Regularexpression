#Problem Statement: Write a function that counts the number of words in a given string.
#Words are defined as sequences of alphanumeric characters separated by spaces or punctuation.
import re

def count_words(text):
    # Define the regular expression pattern to match words
    pattern = r'\w+'
    # Find all matches of the pattern in the text
    words = re.findall(pattern, text)
    # Return the number of words found
    return len(words)

# Test case
text = "Hello, my name is Pradnya Narwade."
print(count_words(text))  

#output:-6
