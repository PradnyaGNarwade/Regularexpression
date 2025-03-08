#9. Find All IP Addresses in a String
#Problem Statement: Write a function to extract all valid IPv4 addresses from a given string.
#An IPv4 address has the form X.X.X.X, where X is a number between 0 and 255.


import re

def extract_valid_ips(text):
    # Define the regular expression pattern to match potential IP addresses
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    # Find all matches of the pattern in the text
    potential_ips = re.findall(pattern, text)
    # Filter out invalid IP addresses
    valid_ips = [ip for ip in potential_ips if all(0 <= int(part) <= 255 for part in ip.split('.'))]
    return valid_ips

# Test case
text = "The server's IPs are 192.168.0.1, 10.0.0.255, and an invalid IP 999.999.999.999."
print(extract_valid_ips(text))

# Output: ['192.168.0.1', '10.0.0.255']
