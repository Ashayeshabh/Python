import re
phone1='9735432100'
pattern1=r'^\d{10}$'
if re.match(pattern1,phone1):
    print("Pattern is Valid")
else:
    print("Pattern is Invalid")