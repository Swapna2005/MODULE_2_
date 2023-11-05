import re

# Sample strings
strings = ['ac', 'abc', 'abbc', 'abbbc', 'abbbbc', 'ad']

# Define the pattern
pattern = r'ab*'

# Check for matches
for string in strings:
    if re.match(pattern, string):
        print(f"String '{string}' matches the pattern.")
    else:
        print(f"String '{string}' does not match the pattern.")
