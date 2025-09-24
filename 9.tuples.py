# coordinates=("x","y")
# my_tuple=(10,20,30)
# print(my_tuple)
# print(type(my_tuple))

#creating  tuple:

#empty tuple:
# Et =()
#tuple  with strings:
# S = ("A","B","C","a","b","c")
#tuple with mixed datatype
# m=(24,3,14,"A","c",True,"False")
#tuple with single element
# a=10
# print(type(a))
# b=[10]
# print(type(b))
# c=(10,)
# print(type(c))

#accesing elements:
# A=(10,20,30,40)
# #+  0   1   2   3
# #- -4   -3 -2 -1
# print(A[0]) #10
# print(A[1]) #20
# print(A[2]) #30
# print(A[3]) #40
# print(A[-1]) #40
# print(A[-2]) #30
# print(A[-3]) #20
# print(A[-4]) #10

#SLICING THE TUPLE:
# a=(10,20,30,40)
# print(a[1:3]) #20 30
# print(a[ :2])  #10 20
# print(a[-3:-1])  #20 30

#changing the values
# tup1 = (50,)
# print(tup1)
# tup1.append(27)
# print(tup1)
# op: 'tuple' object has no attribute 'append'

#length in tuple
# tup1=(10,20,30,44,55,66,77,87)
# print(len(tup1))

#max
# tup1=(10,20,30,44,55,66,77,87)
# print(max(tup1))

#MIN
# tup1=(10,20,30,44,55,66,77,87)
# print(min(tup1))

#sum
# tup1=(10,20,30,44,55,66,77,87)
# print(sum(tup1))

#concatenation:
# a=(10,20)
# b=(12,12)
# c=(a+b)
# print(c)

#repetitiom
# tup1=(10,20,30,40)
# n=int(input("ENTER THE VALUE TO MULTIPLY"))
# b=tup1*n
# print(b)

# searching and cheking in tuple
# fruits = ("apple","bananna","mango")
# print("apple" in fruits)
# print("pineapple" in fruits)
# print("mango" not in fruits)
# print("dragon" not in fruits)

# index():
# tup1=(10,20,30,40)
# print(tup1.index(10))
# print(tup1.index(20))
# print(tup1.index(30))
# print(tup1.index(40))

#count():
# tup1=(10,20,20,20,30,30,40,40,40,40)
# print(tup1.count(10))
# print(tup1.count(20))
# print(tup1.count(30))
# print(tup1.count(40))

#sorting and reversing:
# st=(10,12,23,45,66,23,11,55,52,34,1,77)
# st.sort
# print(st)
# st.reverse