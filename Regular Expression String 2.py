import re
s="_123.456@gmail.com"
pattern=r'^[_0-9]+\.[0-9]+@[a-z]+\.[a-z]+$'
if re.match(pattern,s):
    print("pattern is valid")
else:
    print("pattern is invalid")