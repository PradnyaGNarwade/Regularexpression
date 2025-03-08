#2.Problem Statement: Write a function to check whether a given string is a valid phone number in the format (XXX) XXX-XXXX.
import re

def is_valid_phone_number(phone):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

# Test cases
print(is_valid_phone_number("(123) 456-7890"))  # Output: True
print(is_valid_phone_number("123-456-7890")) 

#output:-
        True
        False
