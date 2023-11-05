import re

# Sample strings
strings = ['123', '567890', '12a34', '9', '1234567', '']

# Define the pattern
pattern = r'^[0-9]{1,6}$'

# Check for matches
for string in strings:
    if re.match(pattern, string):
        print(f"String '{string}' matches the pattern.")
    else:
        print(f"String '{string}' does not match the pattern.")
