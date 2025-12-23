import re
email3='Test_132.ab125@gmail.co.in'
pattern3=r'^[_ A-Z a-z 0-9]+\.[a-z 0-9]+@[a-z]+\.[a-z]+\.[a-z]+$'
if re.match(pattern3,email3):
    print("Email is Valid")
else:
    print("Email is Invalid")