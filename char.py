char=str(input("enter the char"))
if char>="a" and char<="z" or char<"A" and char<="Z":
    print("it is char")       
number=float(input("enter the number"))
if number>=0 and number<=200:
    print("it is digit")        
specialchar=input("enter the specialchar")
if specialchar!=char and specialchar!=number:
    print("it is specialchar")
else:
    print("it is not digit")    
     







