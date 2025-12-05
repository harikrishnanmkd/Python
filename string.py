# str="Hello World!"
# print(str)


# print("Slice :",str[0:5])
# print("Negative Indices :",str[-6:-1])
# print("Skipping charaacters :",str[0:12:2])
# print("Reversing :",str[::-1])


# # Modifying strings
# print("\nModifying String\n")
# str2="Hello World"
# new_str2=str2.replace("World","Python")
# print(str2)
# print("Modified String : ",new_str2)


# # string concatenation

# s1="Hello"
# s2="World"
# result= s1 +", "+ s2 +"!"
# print(result)


# # join method

# words=["Hi", "Hari,","How are you?"]
# sentence=" ".join(words)
# print(sentence)


# String format

# %operator
# name="Hari"
# age=24
# formatted_string= "My name is %s, and Iam %d years old" %(name,age)
# print(formatted_string)

# # format method
# name="Hari"
# age=24
# formatted_string= "My name is {}, and Iam {} years old" .format(name,age)
# print(formatted_string)

# # keyword arguments
# print("My name is {n}, and Iam {a} years old" .format(n="Hari",a=24))

# # f string method

# name="Hari"
# age=24
# print(f"My name is {name}, and Iam {age} years old") 

# string methods

s=" Hello, world "
a="Hello, world world"
print(s)
print("Length",len(s))
print("Word after removing whitespace : ",s.strip())

# split
print(s.split(","))

# find
print(s.find("o"))

# count
print(a.count("world")) 

# startwith
print(s.startswith("Hello"))
print(a.startswith("Hello"))

# endwith
print(a.endswith("world"))
print(s.endswith("world"))





 