# function

# def greet():
#     print("Hello")
# greet()

# def greet(name):
#     print(f"Hello {name}")
# greet("Hari")

# def add(num):
#     print(f"Addition: {num}")
# add(51+2)

# def sum(a,b):
#     sum=a+b
#     print(f"Addition: {sum}")
# sum(52,2)

# positional argument
# def display(name,age):
#     print(f"Hello Iam {name} and i am {age} years old")
# display("Hari",24)

# keyword argument
# def display(name,age):
#     print(f"Hello Iam {name} and i am {age} years old")
# display(name="Hari",age=24)

# default argument
# def display(name,age=24):
#     print(f"Hello Iam {name} and i am {age} years old")
# display(name="Hari")

# return 
# def multiply(a,b):
#     return a*b
# res=multiply(10,20)
# print("Multiply:",res)

# doc string 
# def multiply(a,b):
#     """This line is to multiply"""
#     return a*b
# res=multiply(10,20)
# print(multiply.__doc__)

# lambdafunction
# add=lambda x,y:x+y
# print("Addition:",add(2,3))

# lambda function using map,reduce and filter
# map 
# num=[1,2,3,4]
# square=map(lambda x:x**2, num)
# print(list(square))

#  filter
# num=[1,2,3,4,5,6]
# even=filter(lambda x:x%2==0, num)
# print(list(even))

# reduce
# from functools import reduce
# num=[1,2,3,4,5,6]
# add=reduce(lambda x,y:x+y, num)
# print(add)


# higher order function 

# def calculate(a,b,operation):
#         return operation(a,b)
# def add(a,b):
#         return a+b
# def sub(a,b):
#         return a-b
# def mul(a,b):
#         return a*b
# def div(a,b):
#         return a/b
# print(calculate(9,3,mul))
# print(calculate(9,3,add))
# print(calculate(9,3,sub))
# print(calculate(9,3,div))



# higher order function using lambda 

# def calculate(a,b,operation):
#         return operation(a,b)
# add=lambda a,b:a+b
# sub=lambda a,b:a-b
# print(calculate(9,3,add))
# print(calculate(9,3,sub))

# function scope
# x=10
# def outer_function():
#     x=5
#     # print(x)
#     def inner_function():
#         x=2
#         print(x)
#     inner_function()
# outer_function()
# print(x)

# arbitrary arguments 
# def sum_numbers(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# result=sum_numbers(2,3,4,6,7,8,9)
# print(result)


# keyword argumwnts 
def details(**kwargs):
    for keys,values in kwargs.items():
        print(f"{keys}:{values}")
details(Name="Hari",Age=24,Place="Mannarkkad",District="Palakkad")


def display(a,*args,**karg):
    print("Positional argumrnt:",a)
    print("Arbitrary Positional argumrnt:",args)
    print("Keyword Positional argumrnt:",karg)
display(1,2,3,4,Name="Hari",Age=24)
    








