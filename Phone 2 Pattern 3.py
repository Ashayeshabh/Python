import re
phone2='+91-9735432100'
pattern3=r'^(\+91-)?\d{10}$'
if re.match(pattern3,phone2):
    print("Pattern is Valid")
else:
    print("Pattern is Invalid")