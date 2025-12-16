import array as k
y=k.array("i")
for i in range(0,10):
    value=int(input("enter a value"))
    y.append(value)
p=max(y)
r=min(y)
print(p)
print(r)

    