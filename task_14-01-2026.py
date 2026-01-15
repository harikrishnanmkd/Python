#You are given an array of positive integers. Your task is to reverse the digits of each element in
# the array without the use of built-in functions and return a new array with these reversed
# numbers.(Use any language.)

# def reverse_digits(n):
#     reverse_arr=[]
#     for num in n:
#         rev=0
#         while num>0:
#             dt=num%10
#             rev=rev*10+dt
#             num//=10
#         reverse_arr.append(rev)
#     print(f"Reverse:{(reverse_arr)}\n")
# n=[12,23,54]
# reverse_digits(n)


#Write a program to print the Butterfly Pattern like given below:
# n=int(input("Enter no. of rows:"))
# for i in range(1, n + 1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)
# for k in range(n,0,-1):
#     print("*" * k + " " * (2 * (n - k)) + "*" * k)
    
#Write a program bn3that takes a list of integers and a target sum. Return all unique pairs of
# numbers from the list that add up to the target.
# def unq_pair(num,tar):
#     pairs=[]
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             if num[i]+num[j]==tar:
#                 pair=(num[i],num[j]) 
#                 if pair not in pairs:
#                    pairs.append(pair)  
#     return pairs
# nums = [0, -1, 2, -3, 1]
# target = -2   
# print(f"unique pair:{unq_pair(nums,target)  }\n") 


#A Happy Number is a number defined by the following process:
# 1. Starting with any positive integer,
# 2. Replace the number by the sum of the squares of its digits,
# 3. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly
# in a cycle that does not include 1.
# If it ends in 1, it is a Happy Number
# def happy_no(n):
#    ckd = []
#    while n != 1 and n not in ckd:
#        ckd.append(n)
#        sum_of_square = 0

#        while n > 0:
#           digit = n % 10
#           sum_of_square  += digit * digit
#           n //= 10

#        n = sum_of_square 

#    if n == 1:
#     return True
#    else:
#       return False
# num=int(input("Enter number:"))
# print(f"Happy Number or not:{happy_no(num)}")  
