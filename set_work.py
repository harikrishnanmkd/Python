# 1.Create a set with values {1, 2, 3, 4} .
set1={1,2,3,4}
print("Set=",set1)

# 2. Add the value 5 to the set {1, 2, 3, 4} using a set method.
set1={1,2,3,4}
set1.add(5)
print("new set:",set1)

# 3.Remove the value 3 from the set {1, 2, 3, 4} using a set method.
sett={1,2,3,4}
sett.remove(3)
print("New set after Removing:",sett)

# 4. Check if 2 exists in the set {1, 2, 3, 4}
set1={1,2,3,4}
print("If 2 exists in set:",2 in set1)

# 5.Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.
lt=[1,2,2,3,4,4]
sett=set([1,2,2,3,4,4])
print("New set:",sett)

# 6. Convert the tuple (10, 20, 30) into a set.
tp=(10, 20, 30)
sett=set(tp)
print("Set:",sett)

# 7.Find the union of sets {1, 2, 3} and {3, 4, 5} .
set1={1, 2, 3}
set2={3, 4, 5}
new_set=set1.union(set2)
print("Union:",new_set)

# 8.Find the intersection of sets {1, 2, 3} and {3, 4, 5}
set1={1, 2, 3}
set2={3, 4, 5}
new_set=set1&set2
print("Intersection:",new_set)

# 9. Find the difference between sets {1, 2, 3, 4} and {3, 4}
set1={1, 2, 3, 4} 
set2={3, 4}
new_set=set1-set2
print("Difference=",new_set)

# 10.Create a copy of the set {5, 6, 7} using a set method.
sett= {5, 6, 7}
set2=sett.copy()
print("copy set:",set2)

# 11. Remove all elements from the set {1, 2, 3} using one set method.
sett={1,2,3}
sett.clear()
print("Set after removing all elemets:",sett)

# 12.Check whether {1,2} is a subset of {1,2,3}
set1={1,2}
set2={1,2,3}
print("Subset:",set1.issubset(set2))

# 13.Check whether {1,2,3} is a superset of{1,2}
set1={1,2,3}
set2={1,2}
print("Superset:",set1.issuperset(set2))

# 14.Find the symmetric difference between {1, 2, 3} and {3,4,5}
set1={1, 2, 3}
set2= {3,4,5}
res=set1^set2
print("Symmetric difference:",res)

# 15. Add multiple elements {8, 9, 10} into  {1, 2, 3} using a set method.
sett={1, 2, 3} 
sett.update([8,9,10])
print("updated set:",sett)


# 16.Remove a random element from the set {1, 2, 3} using a set method.
sett={1,2,3}
removed_item=sett.pop()
print("Removed item:",removed_item)
print("New set:",sett)

# 17.Check if two sets {1, 2, 3} and {3, 2, 1} are equal.
seta={1,2,3}
setb={3,2,1}
print("If seta=setb:",seta==setb)

# 18. From the list [1, 2, 2, 3, 4, 4, 5] , extract only unique values using a set.
lt=[1, 2, 2, 3, 4, 4, 5]
sett=set(lt)
print("Unique values:",sett)

# 19.Convert the set {1, 2, 3} into a list.
set={1,2,3}
lt=list(set)
print("List:",lt)

# 20.  From {1, 2, 3, 4, 5} , remove {2, 4} using a set method.
sett={1,2,3,4,5}
setb={2,4}
res=sett-setb
print("New set:",res)