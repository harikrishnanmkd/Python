# # 1.Write a function that takes a number as input and returns whether the number is even or odd 
# a=int(input("Enter number:"))
# def oddeven(a):
#     if a%2==0:
#         return f"{a} is even"
#     else:
#         return f"{a} is odd"
# print(oddeven(a))

# # 2. Write a function that takes three numbers as input and returns the largest number among them
# print("\n2nd")
# a=int(input("Enter first num:"))
# b=int(input("Enter second num:"))
# c=int(input("Enter third num:"))
# def largestnum(a, b, c):
#     if a > b and a > c:
#         return f"{a} is greater"
#     elif b > a and b > c:
#         return f"{b} is greater"
#     else:
#         return f"{c} is greater"
# print(largestnum(a,b,c))

# # 3. Write a function that takes a list of numbers as input and returns the sum of all elements in the list.
# print("\n3rd")
# num=list(map(int,input("Enter numbers:").split(",")))
# def sum_numbers(num):
#     total=0
#     for i in num:
#         total+=i
#     return total
# result=sum_numbers(num)
# print("sum=",result)

# # 4. Write a function that takes a list of numbers as input and returns a new list containing only even numbers
# print("\n4th")
# num=list(map(int,input("Enter numbers:").split(",")))
# def even(num):
#     even=[]
#     for i in num:
#         if i%2==0:
#             even.append(i)
#     return even
# res=even(num)
# print("Given list:",num)
# print("Even nos:",res)

# # 5. Write a function that takes a string as input and returns the length of the string
# print("\n5th")
# str=input("Enter string:")
# def len(str):
#     count=0
#     for i in str:
#         count+=1
#     return count
# res=len(str)
# print(f"Length of {str}:",res)

# # 6. Write a function that takes a string as input and returns the string in uppercase
# print("\n6th")
# str=input("Enter string:")
# def up(str):
#     return str.upper()
# print(f"Uppercase of {str}:",up(str))

# # 7. Write a function that takes a number as input and returns whether the number is positive, negative, or zero
# print("\n7th")
# a=int(input("Enter number:"))
# def number(num):
#     if num>0:
#         return "Number is Positive"
#     elif num<0:
#         return "Number is Negative"
#     else:
#         return "Number is zero"
# print(number(a))

# # 8. Write a function that takes a number as input and returns True if the number is a multiple of both 3 and 5 , otherwise returns False
# print("\n8th")
# a=int(input("Enter number:"))
# def mul(num):
#     if num%3==0 and num%5==0:
#         return True
#     else:
#         return False
# print(mul(a))

# # 9. Write a function that takes a list of numbers as input and returns the maximum value in the list.
# print("\n9th")
# nos=list(map(int,input("Enter numbers:").split(",")))
# def max(num):
#     max_no=num[0]
#     for i in num:
#         if i>max_no:
#             max_no=i
#     return max_no
# print(f"Max value:",max(nos))

# 10. Write a function that takes marks as input and returns the grade according to the following rules:
# A for marks ≥ 90
# B for marks ≥ 75
# C for marks ≥ 60
# Fail for marks below 60
print("\n10th")

mark=int(input("Enter mark : "))
def grade(mark):
    if mark>=90:
        return f"{mark} = A"
    elif mark>=75:
         return f"{mark} = B"
    elif mark>=60:
         return f"{mark} = C"
    else:
          return f"{mark} = Fail"
print(grade(mark))

# 11. Write a function that takes a price as input and returns the discounted price after applying a 10% discount
print("\n11th")
price=float(input("Enter the Price:"))
def discount(p):
    F=p*0.9
    return F
print("Discount price:",discount(price))

# 12. Write a function that takes a list of numbers as input and returns the count of even and odd numbers
print("\n12th")
nos=list(map(int,input("Enter numbers:").split()))
def count(nos):
    even=0
    odd=0
    for i in nos:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
print("Count of even nos and odd nos:",count(nos))

# 13. Write a function that takes a temperature in Celsius as input and returns the temperature in Fahrenheit
print("\n13th")
temp=float(input("Enter the Temperature in Celsius:"))
def c_to_f(c):
    Fahrenheit=(c*1.8)+32
    return Fahrenheit
print("Temperature in Fahrenheit:",c_to_f(temp))