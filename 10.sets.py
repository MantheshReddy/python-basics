# sets:

#unique values only:
# a={1,2,3,3,2,2,1,1,1,2}
# print(a)

#creating aset:
# s1 = {1,2,3}
# s2 = {10,20,5,"Hello",True}
# s3 = {}
# s4=set()
# print(s1)
# print(type(s1))
# print(s2)
# print(type(s2))
# print(s3)
# print(type(s3))
# print(s4)
# print(type(s4))

#accesing sets:
# A = {"name" , "manthesh" , "25N31A66M0"}
# for role in A:
#     print(role)

#adding an element in sets:
# s = {12,18,20}
# s.add(25)
# s.update([35,29])
# print(s)

#deleting the element in set:
# s={35, 12, 18, 20, 25, 29,25}
# s.remove(26)
# print(s)

#DISCARD
# s={35, 12, 18, 20, 25, 29,25}
# s.discard(26)
# print(s)

#pop
# s={35, 12, 18, 20, 25, 29,25}
# s.pop()
# print(s)

#clear:
# s={35, 12, 18, 20, 25, 29,25}
# s.clear()
# print(s)

#mathmatical operations in sets:
#UNION
# A={1,2,3}
# B={4,5,6}
# print(A|B)

#INTERSECTION "n" = "&" :
# A = {1,2,3,4,6}
# B = {4,5,6}
# print(A&B)                

#DIFFERENCE 
# A={1,2,3,4}
# B={3,4,5,6}
# print(A-B)
# print(B-A)

#symmetric difference
# A={1,2,3,4}
# B={3,4,5,6}
# print(A^B)

#mathmatical operations USING FUNCTIONS
# A={1,2,3,4}
# B={3,4,5,6}

# #UNION:
# print(A.union(B))

# #INTERSECTION
# print(A.intersection(B))

# #DIFFERENCE
# print(A.difference(B))

# #SYMMETRIC DIFFERENCE
# print(A.symmetric_difference(B))

# LEN , MAX , MIN , SUM , SORT
#LEN():
# S={10,15,82,96,22}
# print(len(S))#5
# #MAX():
# S={10,15,82,96,22}
# print(max(S))#96
# #MIN():
# S={10,15,82,96,22}
# print(min(S))#10
# #SUM():
# S={10,15,82,96,22}
# print(sum(S))#225
# #SORT():
# S={10,15,82,96,22}
# print(sort(S))# ERROR
