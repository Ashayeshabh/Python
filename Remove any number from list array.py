x=[]
for i in range(0,10):
    value=int(input("enter integer value"))
    x.append(value)
    print(x)
x.insert(5,500)
x.insert(6,600)
x.append(1000)
x.append(2000)
x.remove(1000)
for i in range(0,14):
    print(x[i])