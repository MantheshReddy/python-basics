#LISTS

#COLLECTIONS DATA TYPES

# list1 = [10,20,30,40,50]
# print(list1)
# list2 = ["apple","bananna","mango"]
# print(list2)
# list3 = [10.1,20.2,30.3,40.4,50.5]
# print(list3)
# list4 =[True,False,True,True]
# print(list4)
# list5 =[10,20.5,"hello",True,"False"]
# print(list5)

#accessing elements
#ex:        0  1  2  3  4            (n-1)
# list1 = [10,20,30,40,50]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# #negitive input values
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])

# #slicing in accessing elements
# list1 = [10,20,30,40,50]
# print(list1[0:1])
# print(list1[2:4])
# print(list1[1:4])
# print(list1[3:4])
# print(list1[0:])
# print(list1[ :4])
# #negitive values in slicing
# print(list1[-1: ])
# print(list1[:-4])
# print(list1[:-2])
# print(list1[-3:])
# print(list1[-2:])

#adding elements in list

#append
# list1=[2,4,12,24,25]
# print(list1)
# list1.append(27)
# print(list1)

# fruits=["mango","bananna","grapes","dragon"]
# print(fruits)
# fruits.append("apple")
# print(fruits)

# insert
# list1=[2,4,12,24,25]
# print(list1)
# list1.insert(2,27)
# print(list1)

#extending
# list1=[2,4,12,24,25]
# print(list1)
# list1.extend([27,29,35])
# print(list1)

# adding 26 after 25 after extendng
# list1=[2,4,12,24,25,27,29,35]
# print(list1)
# list1.insert(5,26)
# print(list1)

# removing the elements in the list

#remove
# list1=[2,4,12,24,25,27,29,35]
# print(list1)
# list1.remove(12)
# print(list1)

# #pop
# list1=[2,4,12,24,25,27,29,35]
# print(list1)
# list1.pop(4)
# print(list1)

# #clear  # removes every thing
# list1=[2,4,12,24,25,27,29,35]
# print(list1)
# list1.clear()
# print(list1)

#changing the elements
# list1=[2,4,12,24,25]
# print(list1)
# list1[1]=3
# print(list1)
# list1[4]=27
# print(list1)

#mathematical operations in lists

#1, concatenation
# a=[1,2]
# b=[3,4]
# c=(a+b)
# print(c)

#2, repetition

# a=[1,2]
# n=int(input("Enter The Value Of n"))
# b=a*n
# print(b)

#searching and checking

#in operator:
# a=[2,4,6,8,10,12,14]
# print(3 in a)
# if 2 in a:
#     print("yes item is present in list")

#not in operator:
# a=[2,4,6,8,10,12,14]
# print(3 not in a)

#index():
# a=[2,4,6,8,10,12,14]
# print(a.index(8))

#count():
# a=[2,4,6,8,10,12,14]
# print(a.count(8))
# cnt = 0
# for i in range(10):
#     if i == 8:
#         cnt = cnt + 1
# print(cnt)        

#sorting: sort()
# st = [25,12,5,31,13,18,7,45,8,55,68]
# print(st)
# st.sort()
# print(st)

#reverse:
# st = [25,12,5,31,13,18,7,45,8,55,68]
# st.reverse()
# st.sort()
# print(st)
# st.reverse()
# print(st)

#COPYING THE LIST:

# frd1 = ["A","C","D","A","D","B","B","C","C","A","A"]
# frd2 = frd1.copy()
# frd2[2]="A"
# print(frd2)

#bult-in functions with loops

# st = [25,12,5,31,13,18,7,45,8,55,68]
# #len():returns the number of elements
# print(len(st))
# #max():return the maximumelements from the list
# print(max(st))
# #min():return the minimum elements from list.
# print(min(st))
# #sum():return the total sum of all numeric elements
# print(sum(st))

# string values
# a="hello world to the world python programing"
# b=a.split()
# print(b)

#multiple values using input data to the list
# a = list(map(int, input("enter the multiple values: ").split()))
# a.sort()
# print(a)
# b=input("enter the multiple values:").split()
# print(b)

# #traversing a list
#accesing elements using a loop
#using for looop
# cars=["thar","jaguer","audi","bmw"]
# for car in cars:
#     print("cars =",car)

#using index with for loop:
# list1=[]
# n=int(input("enter the number of list values"))
# for i in range(n):
#     a=input("enter the list values")
#     list1.append(a)
# print(list1)    

#give the input values from 0 to 10
# list1=[]
# for i in range(0,11):
#     list1.append(i)
# print(list1)


# sum of list iteams = 10 20 30 40 50without sum():

# list1=[10,20,30,40,50]
# sum=0
# for i in list1:
#     sum = sum+i
# print(sum)    

# multipication of list terms
# list1=[10,20,30,40,50]
# sum=1
# for i in list1:
#     sum = sum*i
# print(sum) 


#convert ["p","y","t","h","o","n"] into python
# list1= ["p","y","t","h","o","n"]
# sum=""
# for i in list1:
#     sum=sum+i
# print(sum)

#finding maximuma nd minimum values without using max() and min().
# list1=[1,3,6,7,9,12,34,56,79,82]
# list1.sort
# print(list1)
# print("maximum of list 1 is", list1[9])
# print("minimum of list 1 is", list1[0])

#finding maximuma nd minimum values without using max() and min().and sort
# list1 = [52,7,18,12,31,45,17,10,23,229,227]
# max1= list1[0]
# min1=list1[0]
# for num in list1:
#     if num > max1:
#         max1=num
#     if num < min1:
#         min1 = num


#searching for an element in a list
# Names = ["Malla reddy","Revanth reddy","modi","Rahul gandhi"]
# Searching_name=input("enter the name to be found:")
# found=False
# for i in Names:
#     if Searching_name == i:
#         found =True

# if found:
#     print("yes")
# else:
#     print("no")

#count of even and odd numbers
# numbers=[7,10,12,17,18,23,31,45,277,229]
# evn_cnt=0
# odd_cnt=0
# for i in range(len(numbers)):
#     if numbers[i]%2==0:
#         evn_cnt +=1
#     else:
#         odd_cnt += 1
# print("NUMER OF EVEN NUMBERS ARE:",evn_cnt)
# print("NUMBER OF ODD NUMBERS ARE:",odd_cnt)


#REVERING THE LIST WITHOUT revers:
# list1=[7,10,12,17,18,23,31,45,277,229]
# l = len(list1)
# r_list=[]
# for i in range(l-1,-1,-1):
#     r_list.append(list1[i])
# print(r_list)

#removing all negative numbers using loop
# numbers=[-56,-9,2,-8,-30,30,45,23,-19,72,-55,-18,7]
# positive_list=[]
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         positive_list.append(numbers[i])
# print(positive_list)

#multiply each element in list
# list1=[7,10,12,17,18,23,31,45,277,229]
# multiply_list1=[]
# m=int(input("ENTER THE VALUE TO MULTIPLY"))
# for i in range(len(list1)):
#     if list1[i] > 0:
#         multiply_list1.append(list1[i]*m)
# print(multiply_list1)


# write a program to find the average of all numbers in a list----+
#count how many positive , negative and zero values are in a list
#remove duplicate elements from a list.
#write a program to separate even and odd numbers into two new lists.
#take a list of names of names and print the longest name
