i=int(input("enter the number"))
b=i
a=0
while i>0:
    a=(a*10)+i%10
    i//=10
if a==b:
    print(b,"palindrom")
else:
    print(b,"not palindrom")