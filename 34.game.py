b=1
while b<=10:
    c=int(input("enter the number"))
    if c==5:
        print("waah! apne number guess kar liya")
        break
    elif c>5:
        print("apka number bada hai,ek bar or try karo")
    else:
        print("apka number chota hai,ek bar or try karo")
    b=b+1