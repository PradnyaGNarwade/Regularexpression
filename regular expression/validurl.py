#4.Problem Statement: Write a function to validate if a given URL is in the format http:// or https:// followed by a valid domain name and an optional path.
 

import re

def is_valid_url(url):
    pattern = r'^(https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9/._-]*)?)$'
    return bool(re.match(pattern, url))

# Test cases
print(is_valid_url("https://www.example.com/path/to/page"))  # Output: True
print(is_valid_url("ftp://example.com"))  

#Output:-True
#        False
