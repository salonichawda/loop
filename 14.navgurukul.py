i=1
while i<=100:
    if i%3==0:
        print("Nav")
    elif i%7==0:
        print("gurukul")
    elif i%3==0 and i%7==0:
        print("Navgurukul")
    else:
        print(i)
    i=i+1