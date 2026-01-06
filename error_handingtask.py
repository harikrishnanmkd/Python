# 9. Write a program to handle a ValueError when the user enters invalid input (for
# example, entering letters instead of a number).
try:    
    num = int(input("Enter a number: "))
    print("Number=", num)
except ValueError:
    print("Invalid input! Please enter a  number instead of letters.")
    
    
# 10. Write a program to handle invalid input (user enters a string instead of a
# number).
try:
    number = int(input("Enter a number: "))
    print("Entered Number:", number)
except ValueError:
    print("Invalid input! Please enter a  number instead of String.")
    
    
# 11. Write a program that handles file not found error while opening a file.
try:
    file = open("u.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found : The file does not exist.")

# 12. Write a program using try , except , and else blocks.    
try:
    num=int(input("Enter a number"))
    res=10/num
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print(f"The result is {res}")

# 13. Write a program using try , except , and finally to ensure a message
# "Program ended" is always printed.
try:
    num=int(input("Enter a number"))
    res=10/num
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print(f"The result is {res}")
finally:
    print("Program Ended")
    