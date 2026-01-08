import re
s="_.$abc.example@$$gmail.com1"
pattern=r'^\_\.\$[a-z]+\.[a-z]+@\$\$[a-z]+\.[a-z 0-9]+$'
if re.match(pattern,s):
    print("pattern is valid")
else:
    print("pattern is invalid")