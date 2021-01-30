num_1=int(input("enter the number"))
num_2=int(input("enter the number"))
num_3=input("enter the sign")
if num_3=="+": 
    print(num_1+num_2)
elif num_3=="-":
    print(num_1-num_2)  
elif num_3=="*": 
     print(num_1*num_2)
elif num_3=="%":
    print(num_1%num_2) 
else:
    print("invalid")             
