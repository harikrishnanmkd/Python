
# 1. Create a list 1,2,3 and add 4 to the end using a list method.

l1=[1,2,3]
l1.append(4)
print("New list after adding new element to the end:",l1, "\n")

# 2. Given [10,20,30] , remove 20 using a list method.
l1=[10,20,30]
l1.remove(20)
print("New list after removing:",l1, "\n" )

# 3. From [5,3,9,1] , sort the list in ascending order using a list method.
l1=[5,3,9,1]
l1.sort()
print("sorted list:",l1, "\n")

# 4. From [1,2,3,4,5] , extract [2,3,4] using slicing only.
list1=[1,2,3,4,5]
print("Extracted list:",list1[1:4], "\n")

# 5.Reverse the list [1,2,3,4] using slicing (no loops).
l1=[1,2,3,4]
l1.reverse()
print("Reverse:",l1, "\n")

# 6.  Combine [1,2] and [3,4] into one list using list operations.
l1=[1,2]
l2=[3,4]
l1.extend(l2)
print("Combined list",l1, "\n")

# 7.  Convert [7,8] into [7,8,7,8] using list operations.
l1=[7,8]
l1.extend(l1)
print("New list", l1, "\n")

# 8.  Check if 3 exists in [1,2,3,4] using a list operator.
li=[1,2,3,4]
res=li.index(3)
print("3 found in position",res, "\n")


# 9. Count how many times 2 appears in [1,2,2,3,2] using a list method.

l1=[1,2,2,3,2]
print("The number 2 appears",l1.count(2),"times in list", "\n")

# 10. Remove the last element from ["a","b","c","d"] using a list method.
list=["a","b","c","d"]
popped_item=list.pop()
print("List after removing the last element:",list, "\n")

# 11.  Insert "x" at index 1 in ["a","b","c"] using a list method.
l1=["a","b","c"]
l1.insert(1,"x")
print("New list:",l1, "\n")

# 12. Replace the element at index 2 in [10,20,30,40] with 99 using indexing.
l1=[10,20,30,40]
l1[2]=99
print("New list:",l1, "\n")

# # 13. convert range(5) into a list using list function
# range=range(5)
# m_list=list(range)
# print("After converting range to list:",m_list)

# 14.  Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6]
l1=[1,2,3,4,5,6]
print("Expected list:",l1[1:6:2], "\n")


# 15. Remove all elements from [1,2,3] using one list method.

l1=[1,2,3]
l1.clear()
print("List after removing all elements:",l1, "\n")

# 16. Copy a list [4,5,6] using only list tools (no modules).

l1=[4,5,6]
copy_list=l1.copy()
print("copy list:", copy_list, "\n")

# 17. Convert [1,2,3] into a nested list [[1,2,3]] using list operations.
l1=[1,2,3]
l2=[l1]
print("Nested list:",l2, "\n")

# 18.Extend [1,2] with [3,4,5] using a list method.
l1=[1,2]
l2=[3,4,5]
l1.extend(l2)
print("List after extend:",l1, "\n")

# 19. Using list repetition, create a list ["hello","hello","hello"]
l1=["hello"]
l2=l1*3
print("List after repetition",str(l2).replace("'",'"'), "\n")

# 20. Remove the element at index 2 from [10,20,30,40] using a list method.
l1=[10,20,30,40]
del l1[2]
print("List after deleting the element:",l1, "\n")


