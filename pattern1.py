# https://www.wscubetech.com/resources/python/programs/pattern

# row = 5
# for i in range(1, row+1):
#     for j in range(row -i ):
#         print(" ", end = " ")
#     for k in range(1,2*i):
#             print("*", end = " ")
#     print(" ")

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# row  = 5
# for i in range(1, row +1):
#     for j in range(1,i):
#         print(j, end=" ")
#     print(" ")

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# row = 5
# for i in range(row,0,-1):
#     for j in range(1,i+1):
#         print(j, end =" ")
#     print( )
#  -----------OR----------
# row = 6
# for i in range(1, row+1):
#     for j in range(1, (row-i)+1):
#         print(j, end = " ")
#     print(" ")

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# row = 5
# for i in range(1, row+1):
#     for j in range(1 , i+1):
#         print(chr(64+j), end = " ")
#     print("")

# A
# A B
# A B C
# A B C D
# A B C D E

# row = 5
# for i in range(1, row+1):
#     for j in range(1, (row-i)+2):
#         print(chr(64+j), end=" ")
#     print("")
# -----------OR----------
# for i in range(row, 0, -1):
#     for j in range(1, i+1):
#         print(chr(64+j), end = " ")
#     print("")

# A B C D E
# A B C D
# A B C
# A B
# A

# row = 5
# num = 1
# for i in range(1, row+1):
#     for j in range(1, i+1):
#         print(num, end = " ")
#         num += 1
#     print("")

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# Factorial

# num = int(input("Enter number"))
# fact = 1
# for i in range(1,num):
#     fact = fact * i
# print(fact)

# Reverse string without using bulit in function or slicing.

# num = "12345"
# rev = " "
# for i in num:
#     rev = i + rev
# print(rev)

# Using Slicing :
# num = "56789"
# rev = num[::-1]
# print(rev)
# ⭐ Simple One-Line Explanation (Interview)

# We reverse the string by prepending each character to the result, so the last character becomes the first.

# Palindrom Check
# name = "nayan"
# n = name == name[::-1]
# print(n)


# Given a string S, create:
# s1 → characters at odd positions
# s2 → characters at even positions
# ⚠️ Important: Positions usually mean 1-based indexing in such questions.
# So:
# Odd places → 1st, 3rd, 5th...
# Even places → 2nd, 4th, 6th...

# alpha = "programming"
# s1 = ""
# s2 = ""
# for i in range(len(alpha)):
#     if (i+1) % 2 == 0 :
#         s1 += alpha[i]
#     else:
#         s2 += alpha[i]
# print(s1,s2)

# arr = [15, 19, 21, 27, 13]
# arr.sort()
# min_diff =
# for i in range(len(arr) - 1):
#     diff = abs(arr[i] - arr[i+1])
#     if diff < min_diff:
#         min_diff = diff
# print(min_diff)


# Count frequency in string

# s = "hhsseuffhshhriiii"
# ch = {}
# for i in s:
#     if i in ch:
#         ch[i] += 1
#     else:
#         ch[i] = 1
# print(ch)


# from collections import Counter
# s = "hhsseuffhshhriiii"
# freq = Counter(s)
# print(freq)


# find prime number between 1,10

# def prime(n):
#     for i in range(1,n+1):
#         count=0
#         if n> 1:
        
#             for j in range(2,i+1):
#                 if i%j==0:
#                  count+=1
#             if count==1:
#                 print(i)
# prime(10)


# Code for showing how to achieve Encapsulation :

# class Student():
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.__marks = marks
#     def getMarks(self,marks):
#         return self.__marks
        
#     def setMarks(self,newmarks):
#         if newmarks <= 100 : 
#             self.__marks = newmarks
#         else : 
#             print("Invalid marks")
#     def display(self):
#         print(f"this is the {self.name} having {self.age} age having marks {self.__marks}") 
# e = Student("Siddesh",56, 99)

# print(e.getMarks())
# e.setMarks(39)
# print(e.getMarks())

# To find the given number is strong number or not
# def fact(n):
#    f = 1 
#    for i in range(1, n+1):
#        f = f * i
#    return f


# def strong(n):
#     temp = n
#     total = 0
#     while temp > 0 :
#         digit = temp % 10
#         total = total + fact(digit)
#         temp = temp//10
#     if n == total:
#         print("strong number")
#     else:
#         print("weak number 😁")
# strong(6)


def fact(n):
    f = 1 
    for i in range(1, n+1):
        f = f * i
    return f
    
# or -------- We can write in this type also which is easy pythonic way, by converting integer into string by which we can iterate number to extract digit and after that using factorial function we can chech total value.

# def fact(n):
#     f = 1 
#     for i in range(1, n+1):
#         f = f * i
#     return f
    
# num = 40585
# total = 0
# for i in str(num):
#     total = total  + fact(int(i))
# if total == num:
#     print("Strong")
# else:
#     print("Weak")
    


# Find Duplicate : 

# num = [3,2,3,4,5,4,3,5,6]
# seen = []
# duplicates = []
# for i in num:
#     if i in seen and i not in duplicates:
#         duplicates.append(i)
#     else: 
#         seen.append(i)
# print(seen,duplicates)