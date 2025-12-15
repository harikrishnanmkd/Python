# Creating Dictionary

# my_dict={"name":"Hari",
#          "age":"24",
#          "place":"Mannarkkad"
#          }
# print("Dictionary:",my_dict)

# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna")
# print("Dictionary:",my_dict1)

# mydict={}
# print("Dict=",mydict)
# print(type(mydict))

# # Accessing Dictionary
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna")
# print("Name:",my_dict["name"])

# # getmethod
# my_dict={"name":"Hari",
#          "age":"24",
#          "place":"Mannarkkad"
#          }
# print("City:",my_dict.get("place"))

# # Changing or adding elements to dict 
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna")
# c_item=my_dict1["name"]="Kichu"
# print("New dict:",my_dict1)

# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna")
# c_item=my_dict1["Course"]="Python"
# print("New dict:",my_dict1)

# # Removing
# # pop
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna")
# my_dict1.pop("age")
# print("New dict:",my_dict1)

# # popitem
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna",course="Python")
# my_dict1.popitem()
# print("New dict:",my_dict1)

# # delete
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna",course="Python")
# del my_dict1
# print("New dict:",my_dict1)

# # delete
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna",course="Python")
# del my_dict1["age"]
# print("New dict:",my_dict1)

# # clear
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna",course="Python")
# my_dict1.clear()
# print("New dict:",my_dict1)

# # copy
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna")
# dict2=my_dict1.copy()
# print("Copy dict:",dict2)

# using dict
# my_dict1=dict(name="Vysh",age=24,place="Perinthalmanna")
# dict2=dict(my_dict1)
# print("Copy dict:",dict2)

# nested dict
my_dict={"person1":{"name":"Hari","age":"24"},
         "person2":{"name":"Vysh","age":"24"}


}
print("Nested Dict:",my_dict)
print("Accessing name of first person:",my_dict["person1"]["name"])


# adding or changing
my_dict={"person1":{"name":"Hari","age":"24"},
         "person2":{"name":"Vysh","age":"24"}


}
add=my_dict["person1"]["city"]="Mannarkkad"
add=my_dict["person2"]["city"]="Perinthalmanna"
print("New dict:",my_dict)

# Dict methods

# keys()
my_dict={"name":"Hari",
          "age":"24",
          "place":"Mannarkkad"
          }
print(my_dict.keys())

#values()
print(my_dict.values())

# items()-  list of all the keyvalue pairs in the dictionary
print(my_dict.items())

# update()
my_dict={"name":"Hari",
          "age":"24",
          "place":"Mannarkkad"
          }
my_dict.update({"age":25,"course":"python"})
print("New Dict:",my_dict)

# fromkeys
keys=["name","age"]
new_dict=dict.fromkeys(keys,"unknown")
print("Dict:",new_dict)

# setdefault
my_dict1=dict(name="Vysh",age=24)
city=my_dict1.setdefault("city","Perinthalmanna")
print(my_dict1)




