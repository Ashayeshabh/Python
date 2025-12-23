import re
phone2='+91-9735432100'
pattern2=r'^\+91-\d{10}$'
if re.match(pattern2,phone2):
    print("Pattern is Valid")
else:
    print("Pattern is Invalid")