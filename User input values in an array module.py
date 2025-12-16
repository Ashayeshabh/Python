import array as k
y=k.array("i")
for i in range(0,10):
    value=int(input("enter a value"))
    y.append(value)
    y.append(0)
    y.append(10)
    print(y)
for k in y:
    print(k)
    