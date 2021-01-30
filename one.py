user=int(input("enter the user"))
if user%8==0:
    print("priyanka")
    if user%16==0:
        print("sharma")
        if user%8==0 and user%16==0:
            print("priyanka sharma")
        else:
            print("not valid") 
    else:
        print("not valid") 
else:
    print("not valid")                  