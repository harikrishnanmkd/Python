# list=[1,2,3,4]
# list1=["apple","banana","cherry","Orange"]
# print(list)
# print(list1)

# # Accessing list

# print(list1[1])
# print(list1[1:3])

# # changing list

# list1[1]="Pineapple"
# print("New List :",list1)

# # append
# list1.append('Jackfruit')
# print(list1)

# # insert
# list1.insert(1,"watermelon")
# print(list1)

# # extent
# l1=["apple"]
# l2=["banana","cherry"]
# l1.extend(l2)
# print(l1)



# list3=["banana","watermelon","apple","cherry","watermelon"]
# print(list3)
# list3.remove("watermelon")
# print("List after removing a specified item :",list3)
# popped_item=list3.pop(1)
# print(popped_item)
# print("List after pop :",list3)

# list methods

# # count
# list=[1,4,2,3,4,4]
# print(list.count(4))

# # list

# list3=["banana","watermelon","apple","cherry","watermelon"]
# print(list3.index("banana"))


# reverse
# list2=[1,4,2,3,4,4]
# list2.reverse()
# print(list2)

# sort

list=[1,3,2,6,5]
list.sort()
print(list)

# sort in descending order

list5=[1,3,2,6,5]
list5.sort(reverse=True)
print(list5)

# copy
og_list=[1,3,2,6,5]
cp_list=og_list.copy()
print(og_list)
print("copy list",cp_list)
