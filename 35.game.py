a=1
while a<=5:
    b=int(input("enter the number"))
    if b==5:
        print("you win")
        break
    elif b<5:
        print("take a one chance")
    else:
        print("out of game")
    a=a+1