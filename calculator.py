a=int(input("Enter first num:"))
operator=input("Select the operator:")
b=int(input("Enter the second number:"))
if operator=="+":
    sum=a+b
    print("Sum of numbers",a,"+",b,"=",sum)
elif operator=="-":
    sub=a-b
    print("Difference of numbers",a,"-",b,"=",sub)
elif operator=="*":
    mul=a*b
    print("Product of numbers",a,"*",b,"=",mul)
elif operator=="/":
    res=a/b if not b==0 else a,"Can't divisible by 0"
    print("Division of numbers",a,"/",b,"=",res)
else:
    print("Invalid")

