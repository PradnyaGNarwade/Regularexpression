#7. Extract All Hashtags from a Text
#Problem Statement: Write a function to extract all hashtags (words starting with #) from a given string.


import re

def extract_hashtagsstring(text):
    # Define the regular expression pattern to match dates
    pattern = r'#\w+'
    # Find all matches of the pattern in the text
    hashtags = re.findall(pattern, text)
    # Return the list of dates found
    return hashtags

# Test case
text = "Loving the weather today! #sunny #goodvibes #relax"
print(extract_hashtagsstring(text))

#Output:-['#sunny', '#goodvibes', '#relax']
