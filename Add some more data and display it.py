import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    ("file doesn't exists")    
file1=open("sample.txt","w")
file1.write("Hello World")
file1.close()