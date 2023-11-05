

# import library
import re
 
# make a pattern
pattern = "^[A-Za-z0-9_-]*$"
 
# input
string = "G33ks_F0r_Geeks"
 
# convert match object 
# into boolean values
state = bool(re.match(pattern, string))
 
print(state)