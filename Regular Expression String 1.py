import re
s="abc_123"
pattern=r'^[_ a-z 0-9]+$'
if re.match(pattern,s):
    print("pattern is valid")
else:
    print("pattern is invalid")