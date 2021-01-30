# num=int(input("enter the num"))
# if num==1:
#     print("it is not prime number")
#     if num%2!=0:
#         print("it is prime number")
#         if num%5!=0:
#             print("it is prime number")
#         else:
#             print("it is prime number")
    
Sex = input("enter sex M\F")
material_status = input("enter the metarial status Y or N")
Age = input("enter a age")
if Sex=="Female":
    if material_status=="y":
        print("she will job in urban area")
    else:
        print("she will not do job")
elif Sex=="Male":
    if material_staus=="y":
        if age>20 and age<40:
            print("he can do work any where")
        elif age>40 and age<60:
            print("he will job in urban area")
        else:
            print("he will not do work")
    else:
        print("he can't")
else:
    print("gender is not valid")