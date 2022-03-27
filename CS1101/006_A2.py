# #Q1 solution
# x = "Abhisruta Maity"

# for i in range(0,15):
#     print(f"{i+1} {x}") #Q1

# #Q2 solution
# x = "Abhisruta Maity"

# for i in range(0,15):
#     if (i+1)%3 == 0:
#         print(f"{i+1} {x}") #Q2

# #Q3 solution
# x = "abcdefghijkl"
# print(x)
# y = list(x)
# for i in range(0, len(y)):
#     del y[0]
#     z = "".join(y)
#     print(z) #Q3

# #Q4 solution
# n1 = [0, 3, 1, 2, 8, 9, 0, 4, 7]
# n2 = [0, -1, -3, -4, 3, 8, 9, 11, -2]
# def maxlist(x):
#     m = x[0]
#     for i in range(0, len(x)):
#         if (x[i] > m):
#             m = x[i]
#     print(f"The maximum of the list {x} is {m}.")
# maxlist(n1)
# maxlist(n2)
# print("\n") #Q4

# #Q5 solution
# n1 = [0, 3, 1, 2, 8, 9, 0, 4, 7]
# n2 = [0, -1, -3, -4, 3, 8, 9, 11, -2]
# def maxlist(x):
#     m = x[0]
#     indexlist = []
#     for i in range(0, len(x)):
#         if (x[i] > m):
#             m = x[i]
            
#     for i in range(0, len(x)):
#         if (x[i] == m):
#             indexlist.append(i+1)
#     print(f"The maximum of the list {x} is {m}. It's indices are {indexlist}") # We count index from 1 as a natural number.
#     print(m == max(x))

# def minlist(x):
#     m = x[0]
#     indexlist = []
#     for i in range(0, len(x)):
#         if (x[i] < m):
#             m = x[i]
            
#     for i in range(0, len(x)):
#         if (x[i] == m):
#             indexlist.append(i+1)
#     print(f"The minimum of the list {x} is {m}. It's indices {indexlist}") # We count index from 1 as a natural number.
#     print(m == min(x))

# maxlist(n1)
# maxlist(n2)
# print("\n")
# minlist(n1)
# minlist(n2)
# print("\n") #Q5

# # #Q6 solution
# name = input("Your Name: ")
# year = input("Year of Joining IISER-K: ")
# courseID = input("Your Course ID: ")
# studentID = input("Your Student ID: ")

# list = [name, year[len(year)-2:len(year):], courseID, f"{studentID}@iiserkol.ac.in"]

# emailID = "-".join(list)
# print(emailID) #Q6

# #Q7 solution
# str1 = '123'
# str2 = '234'
# str3 = '456'

# sum = eval(str1) + eval(str2) + eval(str3)
# product = eval(str1) * eval(str2)* eval(str3)
# average = sum/3

# print(sum, product, average) #Q7

# #Q8 solution
# sum = 0
# for i in range(5):
#     a = int(input(f"Give number {i+1}: "))
#     sum += a
# print(sum) #Q8

# #Q9 solutions
# numlist = []
# for i in range (0,10):
#     b = int(input(f"The marks obtained by student no. {i+1} is: "))
#     numlist.append(b) #stored in "list" variable. #Q9a

# print(list(reversed(sorted(numlist)))) #Q9b

# for i in range(0,len(numlist)):
#     if (numlist[i] < 45):
#         numlist[i] += 5
# print(numlist) #Q9c

# fail_count = 0
# for i in range(0, len(numlist)):
#     if (numlist[i] < 50):
#         fail_count += 1
# print(fail_count) #Q9d

# #Q10 solutions:
# numlist = []
# for i in range(0, 10):
#     c = input(f"Give number {i+1}: ")
#     numlist.append(c) #Q10a

# print(numlist) #Q10b
# print(sorted(numlist)) #Q10c

# newlist = []
# for x in numlist:
#     if x != max(numlist) and x != min(numlist):
#         newlist.append(x)

# print(newlist) #Q10d

#a
from audioop import reverse


mark_list = list(map(int,input("Enter marks of 10 students in a subject separated by a space : ").strip().split()))

#b
print(list(reversed(sorted(mark_list))))

#c
for i in mark_list:
    if (i < 45):
        i += 5
        print(i)
        
print(mark_list)