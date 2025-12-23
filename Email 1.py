import re
email='test123@gmail.com'
pattern=r'^[a-z 0-9]+@[a-z]+\.[a-z]+$'
if re.match(pattern,email):
    print("Email is Valid")
else:
    print("Email is Invalid")