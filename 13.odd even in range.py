a=int(input("enter the number"))
i=1
while i<=100:
    if a%2!=0:
        print("werid")
    elif a%2==0 and i in range(2,5):
        print("Not weird")
    elif a%2==0 and i in range(6,20):
        print("weird")
    elif a%2==0 and a>20:
        print("not weird")
    i=i+1