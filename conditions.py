# if,elif,else

# a=10
# if(a>0):
#     print(a,"is positive")
# elif(a==0):
#     print(a,"is neither positive nor negative")
# else:
#     print(a,"is negative")

# nested if
# x=10
# Y=4
# if(x>5):
#     if(Y<5):
#         print("x is greater than 5 and 4 is less than 5")

# and
# x=10
# y=4
# if(x>5)and(y<5):
#     print("x is greater than 5 and y is less than 5")

# or
# x=10
# y=4
# if(x>5)or(y<5):
#     print(x,"is greater than 5 and",y,"is less than 5")

# not
# x=10
# y=5
# if not(x>5):
#     print(x," is greater than 5")

# ternary operator
# x=10
# result= "x is positive" if x>0  else "x is negative" 
# print(result)

# pass
# a=-10
# if(a>0):
#     pass
# else:
#     print(a,"is negative")


# input
# a=int(input("Enter number: "))
# if(a>0):
#     print(a,"is positive")
# elif(a==0):
#     print(a,"is neither positive nor negative")
# else:
#     print(a,"is negative")

# for loop

# a=int(input("Enter the limit:"))
# for i in range(1,a):
#     print(i)

# break
# a=int(input("Enter the limit:"))
# for i in range(1,a):
#     if i==3:
#         break
#     print(i)   

# continue
a=int(input("Enter the limit:"))
for i in range(1,a):
    if i==3:
        continue
    print(i) 