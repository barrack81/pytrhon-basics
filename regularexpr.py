# in python regular expression is a sequence of characters that forms a search pattern
"""import re as regex
x = regex.search("^a", "apple")
print(x) #output = <re.Match object; span=(0, 1), match='a'>

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")"""
    
import re

txt  = "i have 3 oranges and 5 apples"
x = re.search("\s", txt, 3)
if x:
    print("yes")
else:
    print("no")
