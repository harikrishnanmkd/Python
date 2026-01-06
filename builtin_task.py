# 16. Write a program that uses the math module to find the square root of a
# number.
import math
number = float(input("Enter a number: "))
sqr_root = math.sqrt(number)
print(f"Square root of {number} is: {sqr_root}")

# 17. Write a program that uses the math module to calculate power of a number.
import math
base_no = float(input("Enter the base number: "))
exp_no = float(input("Enter the exponent: "))
result = math.pow(base_no, exp_no)
print(f"{base_no}^{exp_no}: {result}")

# 18. Write a program that uses the math module to find the factorial of a number
import math
num = int(input("Enter a number: "))
fact = math.factorial(num)
print(f"Factorial of {num} is: {fact}")