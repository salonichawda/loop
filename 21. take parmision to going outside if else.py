print("need permission to go outside")
outside=input("enter the place name:")
if outside=="hospital" or outside=="home":
    print("going to outside")
    reason=input("enter the reason:")
    if reason=="fiver" or reason=="headeck" or reason=="allergy" or reason=="porsonal reason":
        print("reason is valid")
        permission1=input("enter the permission which should:")
        if permission1=="team member":
            print("team member gave permission")
            permission2=input("enter the permission:")
            if permission2=="disco":
                print("disco gave permission")
                permission3=input("enter the permission:")
                if permission3=="health cordinator":
                    print("health cordinator gave permission")
                    print("you all gave permission")
                    time=input("enter the time:")
                    if time>="10:00" and time<="5:00":
                        print("come between this time")
                        quarantine=input("enter the will be quaranted or not:")
                        if quarantine=="vaccinated":
                            print("will not quarantine")
                        else:
                            print("you will quarantine")
                    else:
                        print("you got oil you will not come within time")
                else:
                    print("health cordinator not gave permission")
            else:
                print("disco not gave permission")
        else:
            print("team member not gave permission")
    else:
        print("reason is not valid")
else:
    print("somewhere else go")