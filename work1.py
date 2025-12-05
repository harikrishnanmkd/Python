# 1
str="hello"
print("To uppercase : ",str.upper(),"\n")

# 2
str="concatenate"
s=str.find("cat")
print("Cat fount in",s, "rd position of the string","\n")

# 3
str ="I Love Python"
print(str.replace("Python","🐍"),"\n")

# 4
str="bananaa"
print("Count of a :",str.count("a"),"\n")

# 5
str=" space me "
print("String after removing spaces from both-ends :", str.strip(),"\n")

# 6
str="nikthebestie"
print("sliced word:",str[6:10])
print("sliced word using negative index:",str[-6:-2],"\n")

# 7
str="abcdef"
print(f"Reverse of {str} :", str[::-1] ,"\n" )

# 8
str="malayalam"
rev=str[::-1]
print(f"{str} is palindrome :",rev==str)