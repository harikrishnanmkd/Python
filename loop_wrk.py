# a=int(input("Enter the limit:"))
# for i in range(10,a,-1):
#     print(i,"Hari")


# odd or even 
# 1st method 
# a=int(input("Enter the limit:"))
# odd = []
# even = []
# for i in range(1,a):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd number",odd)
# print("Even number",even)

# 2nd method list comphrehension
# limit=int(input("Enter the limit:"))
# a=[x for x in range(1,limit) if x%2==0]
# b=[x for x in range(1,limit) if x%2!=0]
# print("Odd numbers",a)
# print("Even numbers:",b)

# square of odd numbers

limit=int(input("Enter the limit:"))
a=[x**2 for x in range(1,limit) if x%2==0]
b=[x**2 for x in range(1,limit) if x%2!=0]
print("Square of odd numbers",a)
print("Square of even numbers:",b)
 
        
    

