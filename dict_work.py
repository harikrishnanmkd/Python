# 1. Create a dictionary with keys "name" and "age" and values  "Nik" and 20
my_dict={"name":"Nik",
          "age":"20"
}
print("Dictionary:",my_dict)


# 2. Access the value of key "name" from {"name": "Nik", "age": 20"} 
print("Name:",my_dict["name"])

# 3 Add a new key "city" with value "Delhi" to {"name": "Nik", "age": 20}
my_dict["city"]="Delhi"
print("Changed Dict:",my_dict)

# 4. Update the value of "age" to 25 in {"name": "Nik", "age": 20}
dict1={"name": "Nik", "age": 20}
dict1.update({"age":25})
print("Updated Dict:",dict1)


# 5. Delete the key "age" from {"name": "Nik", "age": 20}
dict1={"name": "Nik", "age": 20}
delete=dict1.pop("age")
print("New dict:",dict1)

# 6. Check if the key "email" exists in {"name": "Nik", "age": 20}
dict1={"name": "Nik", "age": 20}
print("if the key email exists in dict1:","email"in dict1)

# 7.Get all keys from {"name": "Nik", "age": 20} using a dictionary method.
dict1={"name": "Nik", "age": 20}
print(dict1.keys())

# 8.Get all values from {"name": "Nik", "age": 20} using a dictionary method.
print(dict1.values())

# 9. Convert the dictionary {"a": 1, "b": 2} into a list of (key, value) pairs.
dict1={"a": 1, "b": 2}
lt=list(my_dict.items())
print("List of key value pair:",lt)

# 10. Create a dictionary from two lists: (use zip method) keys = ["name", "age"] values = ["Nik", 20]
keys = ["name", "age"] 
values = ["Nik", 20]
dict2=dict(zip(keys,values))
print("Dictionary:",dict2)

# 11.Count how many keys are in {"a": 1, "b": 2, "c": 3}
dict1={"a": 1, "b": 2, "c": 3}
count=len(dict1.keys())
print("Count:",count)

# 12.Merge two dictionaries {"a": 1} and {"b": 2} into one.
dict1={"a": 1}
dict2={"b": 2}
dict1.update(dict2)
print("New merged dictionary:",dict1)

# 13. Clear all elements from {"a": 1, "b": 2} using a dictionary method.
dict1={"a": 1, "b": 2}
dict1.clear()
print("Dict:",dict1)

# 14. Copy the dictionary {"x": 10, "y": 20} using a dictionary method.
dict1= {"x": 10, "y": 20}
cp_dict=dict1.copy()
print("copy dictionary:",cp_dict)

# 15. Get the value of key "salary" safely from {"name": "Nik", "age": 20} without getting an error.
my_dict={"name": "Nik", "age": 20}
print("Salary:",my_dict.get("salary"))

# 16. From {"a": 1, "b": 2, "c": 3}, remove the last inserted item using a dictionary method.
my_dict={"a": 1, "b": 2, "c": 3}
item=my_dict.popitem()
print("Popped item:",item)
print("Resultant dictionary:",my_dict)

# 17. Given student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} , access only the "science" marks.
student = {"name": "Rahul", "marks": {"math": 90, "science": 85}}
print("Mark in science:", student["marks"]["science"])

# 18. From the above student dictionary, update "math" marks to 95
update_mark=student["marks"]["math"]=95
print("Updated mark in Maths:",update_mark)

# 19. Add a new subject "english": 88 inside the "marks" dictionary.
new_sub=student["marks"]["english"]=88
print("Updated Dictionary:",student)

# 20. Delete the subject "science" from inside "marks"
del student["marks"]["science"]
print("Dictionary after deletion:",student)
