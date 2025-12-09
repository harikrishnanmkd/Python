# 1.  Create a tuple (1,2,3,4) and access the element 3 using indexing.
tp=(1,2,3,4)
print(tp[2])

# 2. Convert the tuple (10,20,30) into a list.
tp=(10,20,30)
tmp_lst=list(tp)
print("List=",tmp_lst)

# 3. Convert the list [1,2,3] into a tuple.
lt=[1,2,3]
tpl=tuple(lt)
print("Tuple=",tp)


# 4. From the tuple ("a","b","c","d") , extract ("b","c") using slicing
tp=("a","b","c","d")
print(tp[1:3])

# 5. Check if "x" exists inside the tuple ("x","y","z") .
tp=("x","y","z")
res=tp.index("x")
print("x found in position",res)

# 6.Given (5,3,9,1) , find the maximum value using a tuple function.   
tp=(5,3,9,1)
li=list(tp)
li.sort()
tp1=tuple(li)
print("Max value:",tp1[-1]) 

# 7. Given (1,2,3) , create a new tuple (1,2,3,1,2,3) using tuple operations only.
tp=(1,2,3)
tp_1=tp+tp
print("New tuple:",tp_1)

# 8.  Count how many times 2 appears in (1,2,2,3,2) using a tuple method.
tp=(1,2,2,3,2)
print("count=",tp.count(2))

# 9.Find the index of  "cat" in ("dog","cat","mouse") .
tp=("dog","cat","mouse")
print("Index=",tp.index("cat"))

# 10.Reverse (1,2,3,4,5) using slicing.
tp=(1,2,3,4,5)
print("Reverse:",tp[::-1])

# 11. Combine (1,2) and (3,4) into  (1,2,3,4) using tuple operations.
tp=(1,2)
tp1=(3,4)
Joined_tp=tp+tp1
print("Tuple after joining:",Joined_tp)

# 12. Convert "hello" into a tuple of characters
a="hello"
tp=tuple(a)
print("Tuple=",tp)

# 13. Convert (1,2,3,4) into the list (1,4) by extracting only first & last elements.
tp=(1,2,3,4)
print("Extracted tuple=",tp[0:4:3])

# 14. Given a tuple (10,20,30,40) , replace the value 30 with 99 (hint:convert to list → modify → convert back).
tp=(10,20,30,40)
lt=list(tp)
lt[2]=99
tp_new=tuple(lt)
print("After replacing:",tp_new)

# 15.Using unpacking, extract a=1 , b=2 , c=3 from (1,2,3) .
tp=(1,2,3)
(a,b,c)=tp
print("a=",a)
print("b=",b)
print("c=",c)

# 16.Create a nested tuple: turn (1,2,3) into ((1,2,3),) .
tp=(1,2,3)
tp2=(tp,)
print("New tuple=",tp2)

# 17. Merge ("a","b") with  ["c","d"] to get a single tuple ("a","b","c","d") (hint: convert list → tuple).
tp1=("a","b")
lt=["c","d"]
tp2=tuple(lt)
tp3=tp1+tp2
print("New tuple=",str(tp3).replace("'",'"'))

# 18. Check if tuple (1,2,3) is equal to its reverse.
tp=(1,2,3)
print(tp[::-1]==tp)

# 19.  Convert a tuple of lists ([1,2],[3,4]) into a single flat list [1,2,3,4]
tp=([1,2],[3,4])
b=(tp[0]+tp[1])
print(b)

# 20. Given (1, [2,3], 4) , add  5 inside the inner list so result becomes (1, [2,3,5], 4) .

tp=(1,[2,3],4)
tp[1].append(5)
print("New tuple=",tp)
