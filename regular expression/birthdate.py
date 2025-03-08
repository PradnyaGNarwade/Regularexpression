#5. Extract Dates from a String
#Problem Statement: Write a function to extract all dates in the format MM-DD-YYYY from a given string.
import re

def extract_dates(text):
    # Define the regular expression pattern to match dates
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    # Find all matches of the pattern in the text
    dates = re.findall(pattern, text)
    # Return the list of dates found
    return dates

# Test case
text = "My birthday is on 12-11-2004 and my friend's birthday is 01-20-2000."
print(extract_dates(text))

#output:-
['12-11-2004', '01-20-2000']
