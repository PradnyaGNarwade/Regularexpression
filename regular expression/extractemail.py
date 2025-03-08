#Problem Statement: Write a function that extracts all email addresses from a given string.
import re

def find_emails(text):
    # List of email patterns to look for
    patterns = [r"\S+@\S+"]
    
    for pattern in patterns:
        # Compile the pattern
        email_regex = re.compile(pattern)
        
        # Find all instances of the pattern in the text
        emails = email_regex.findall(text)
        
        # Print each email found
        for email in emails:
            print(email)

# Example usage
text = "Please send your resumes on Hr@Iwillgetbacktoyou@gmail.com" \
       "  for any business enquiry please mail us on business@enquiry.com" \
       " and writing.geeksforgeeks.org"
find_emails(text)

#Output:-
#Hr@Iwillgetbacktoyou@gmail.com
#business@enquiry.com
