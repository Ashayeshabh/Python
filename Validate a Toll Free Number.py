import re
tollfreeno='1800-456-7890'
pattern=r'^\d{4}-\d{3}-\d{4}$'
if re.match(pattern,tollfreeno):
    print("Pattern is valid")
else:
    print("Pattern is invalid")