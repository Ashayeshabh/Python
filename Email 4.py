import re
email4="_abc.example.com"
pattern4=r'^[_a-z]+\.[a-z]+\.[a-z]+$'
if re.match(pattern,email):
    print("pattern is valid")
else:
    print("pattern is invalid")