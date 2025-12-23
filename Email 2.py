import re
email2='test_123abc@gmail.com'
pattern2=r'^[_ a-z 0-9]+@[a-z]+\.[a-z]+$'
if re.match(pattern2,email2):
    print("Email is Valid")
else:
    print("Email is Invalid")