import re

# Sample string
string = "hello_world this_is_a_sample_string with_nothing"

# Define the pattern
pattern = r'[a-z]+_[a-z]+'

# Find all matches
matches = re.findall(pattern, string)

# Print the matches
print("Sequences of lowercase letters joined with an underscore:")
for match in matches:
    print(match)
