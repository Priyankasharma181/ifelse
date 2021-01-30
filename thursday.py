day=input("enter the day")
precation=input("enter the precation")
permison=input("enter the y/n")
if day=="thursday":
    print("holiday")
    if precation=="safe":
        print("sentaizer,gloves,maks")
        if permison=="y":
            print("go outside")
        else:
            print("donnt go")
    else:
        print("not safe") 
else:
    print("not holiday")        


 