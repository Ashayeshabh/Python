x=[]
for i in range(0,10):
    value=int(input("enter integer value"))
    x.append(value)
    print(x)
x.append(500)
x.append(600)
x.insert(5,1000)
x.insert(6,2000)
for i in range(0,14):
    print(x[i])