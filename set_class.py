# # creating set

# set0={1,2,3}
# print(set)
# set2=set([1,2,5,4])
# print("set=",set2)

# # Empty set using set funcn
# set3=set()
# print("Null set:",set3)

# # accessing item from set
# set4={"hari","vysh",}
# print("vysh" in set4)


# Add element in set

# # add
# set={1,2,3}
# set.add(5)
# print("new set:",set)

# # update
# sett={1,2,3}
# sett.update([5,6])
# print("New set:",sett)



# # Delete element in set
# # remove
# my_set1={1,2,3,4}
# my_set1.remove(4)
# print(my_set1)

# # discard
# my_set={1,2,3,4}
# my_set.discard(5)
# print(my_set)

# # pop
# my_set3={5,2,3,4,1}
# removed_item=my_set3.pop()
# print("Removed item:",removed_item)
# print("New set:",my_set3)

# # clear
# my_set5={2,3,4,1}
# my_set5.clear()
# print(my_set5)

# # Set operation or joining set
# # union
# set1={1,2,3,4}
# set2={4,5,6,7}
# new_set=set1.union(set2)
# print("Union:",new_set)

# # union using update method
# set1={1,2,3,4}
# set2={4,5,6,7}
# set1.update(set2)
# print("Union(using update):",set1)

# # Intersection
# set1={1,2,3,4,6}
# set2={4,5,6,7}
# new_set=set1&set2
# print("Intersection:",new_set)

# # Set difference
# set1={1,2,3,4,6}
# set2={4,5,6,7}
# new_set=set1-set2
# print("Set difference:",new_set)

# # set symmetric difference
# set1={1,2,3,4,6}
# set2={4,5,6,7}
# new_set=set1^set2
# print("Symmetric difference:",new_set)

# # copy
# set1={1,2,3,4}
# set2=set1.copy()
# print("copy:",set1)


# # subset

# set1={1,2}
# set2={1,2,3,4}
# print("Subset:",set1.issubset(set2))

# set1={1,2}
# set2={1,2,3,4}
# print("Subset:",set2.issubset(set1))

# # superset

# set1={1,2}
# set2={1,2,3,4}
# print("Superset:",set1.issuperset(set2))

# set1={1,2}
# set2={1,2,3,4}
# print("Superset:",set2.issuperset(set1))

# # Frozenset
# set=frozenset([1,2,3,4])
# print("Frozenset:",set)



