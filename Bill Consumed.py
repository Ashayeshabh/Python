x=int(input("enter the unit consumed"))
if x<=100:
    amount=x*4.25
elif x>=101 and x<=200:
    amount=x*6.10
elif x>=201 and x>300:
    amount=x*7.35
elif x>=301 and x<=400:
    amount=x*7.70
elif x>=401 and x<=500:
    amount=x*8.75
elif x>=501 and x<=600:
    amount=x*9.10
elif x>=601 and x<=700:
    amount=x*10.20
else:
    amount=x*11.40
print("Bill amount",amount)    