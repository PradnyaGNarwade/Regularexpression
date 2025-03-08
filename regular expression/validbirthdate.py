#10. Validate a Date in DD-MM-YYYY Format
#Problem Statement: Write a function to validate if a given string represents a valid date in the format DD-MM-YYYY.


import re
from datetime import datetime

def is_valid_date(date_string):
    # Define the regular expression pattern for DD-MM-YYYY format
    pattern = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$'
    
    # Check if the date_string matches the pattern
    if re.match(pattern, date_string):
        try:
            # Attempt to parse the date to check its validity
            day, month, year = map(int, date_string.split('-'))
            datetime(year, month, day)
            return True
        except ValueError:
            # If ValueError occurs, the date is invalid
            return False
    else:
        # If the pattern doesn't match, the format is incorrect
        return False

# Test cases
print(is_valid_date("15-04-2023"))  # Output: True
print(is_valid_date("31-02-2023"))  # Output: False
print(is_valid_date("2023-04-15"))  # Output: False

