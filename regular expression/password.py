#8. Validate a Strong Password
#Problem Statement: Write a function to validate a password. A strong password must meet the following criteria:
#•	Be at least 8 characters long.
#•	Contain both uppercase and lowercase letters.
#•	Contain at least one digit.
#•	Contain at least one special character (e.g., @, #, $).


import re

def is_strong_password(password):
    # Define the regular expression pattern for a strong password
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
    # Use re.match to check if the password matches the pattern
    return bool(re.match(pattern, password))

# Test cases
print(is_strong_password("Strong@123"))  # Output: True
print(is_strong_password("weakpass"))    # Output: False

#output:True
#    False
