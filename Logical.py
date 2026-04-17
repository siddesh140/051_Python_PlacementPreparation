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

# We reversed the string by prepending each character to the result, so the last character becomes the first.

# Palindrom Check

# By using Two Pointer  approach :

# def palindrom(s1):
#     left, right = 0, len(s1) - 1
#     while left < right:
#         if s1[left] != s1[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(palindrom("nayan"))

# By using Slicing method

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
# s1 = alpha[1::2]
# s2 = alpha[::2]


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
#         if n > 1:

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


# or -------- We can write in this type also which is easy pythonic way, by converting integer
# into string by which we can iterate number to extract digit and after that using factorial function we
# can check total value.

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


# To find vowels from given string

# line = "programming"
# vowels = "aeiou"
# only_vowel = []
# for i in line:
#     if i in vowels:
#         only_vowel.append(i)
# print(only_vowel)

# Count Vowels from Given String

# line = "programming"
# vowels = "aeiou"
# count = sum(1 for ch in line if ch in vowels)
# print(count)


# Count occurrences of a character in string

# line = "Programming"
# count1 = line.lower().count("p")
# print(count1)


# To revers number : This following method can be used for charecters string also.

# num = "12345"
# rev = ""
# for i in num:
#     rev = i + rev
# print(rev)

#  method to reverse the integer

# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = (rev * 10) + digit
#     num = num // 10
# print(rev)


# Armstrong Number : a number with n digits, it is an Armstrong number if the sum of each digit raised
# to the power of n equals the original number.

# num = 1634
# count = sum((int(i)**4 for i in str(num)))
# if count == num:
#     print("Its an Armstrong number")
# else:
#     print("Not Armstrong Number")


# Count length of string without using len() function: this will includes all spaces also.

# line = "jfshuiwgfe"
# count = 0
# for i in line:
#     count += 1
# print(count)

# Count the words in the string
# line = "I love Java Programming"
# print(len(line.split()))   #This will only give count of words.


# To find LCM :

# import math
# a,b = 2,5
# print(abs(a*b))

# To find 2nd Highest number

# Here we are removing duplicates by converting list into set and using sorted, set will be in ascending order 
# then by using slicing we can get 2nd highest number

# num = [2,5,4,3,6,7,5,4,4]
# count = sorted(set(num))[-2]
# print(count)

# Without sorting or built in function :
# num = [2,5,4,3,6,7,5,4,4]
# largest = float("-inf")
# second  = float("-inf")

# for i in num:
#     if i > largest:
#         largest = i
#         second = largest
#     elif i > second and i != largest:
#         second = i
# print(second)


# Check Anagram :  Do strings anagram hote hain agar:
# Same characters
# Same frequency
# Order matter nahi karta

# s1 = "silent"
# s2 = "listen"

# By using sorted method:
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else :
#     print("Not Anagram")

# Without using sorted method :
# from collections import Counter
# if Counter(s1) == Counter(s2):
#     print("Anagram")

# def anagram(s1,s2):
#     alpha = [0] * 26
#     if len(s1) != len(s2):
#         return False
#     for i in range(len(s1)):
#         alpha[ord(s1[i].lower()) - ord('a')] += 1
#         alpha[ord(s2[i].lower()) - ord('a')] -= 1

#     for i in alpha:
#         if i != 0:
#             return False
#     return True
# print(anagram("listen","hujjjj"))

# print(ord('A'))  ->  use to convert charecter to integer
# print(chr(65))  -> use to convert integer to charecter


# a = "55-10"
# print(eval(a))

# If want to print only key from the dict

# dict = {"a" : 1, "b" : 2, "c" : 3}
# l_k = list(dict)
# l_k = [*dict]  #using unpacking operator
# l_k = dict.keys()  # using key function
# print(l_k)

# How to unpack List.

# a = [1,2,3,4,5]
# print(*a)


# x = (10, 20, 30)
# print(id(x))
# y = (40, 50, 60)
# x = x + y
# print(id(x))
# print(x)


# Move Zeroes (Easy/Medium)
# Given an array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Why they ask this: It’s the classic Two-Pointer problem (similar to your palindrome logic).

# num = [0, 1, 2, 0, 3, 4]
# slow = 0
# for i in range(len(num)):
#     if num[i] != 0:
#         # swap the elements
#         num[slow], num[i] = num[i], num[slow]
#         slow += 1
# print(num)

# Using Two pointer technique we can maintain time complexity.

# num = [0, 1, 2, 0, 3, 4]
# first = 0
# for second in range(len(num)):
#     if num[second] != 0:
#         num[first], num[second] = num[second], num[first]
#         first += 1

# print(num)

# I use two pointers where one pointer tracks the position for non-zero elements and the other iterates 
# through the array. When a non-zero element is found, I swap it with the position pointed by the first 
# pointer.
    


# Jack loves Sundays. He wants to find out how many Sundays will occur in a month if he knows two things:
# - The day on which the month starts (e.g., Monday, Tuesday, etc.)
# - The total number of days in that month
# Your task is to determine how many Sundays fall in that month based on this information.

# month_start = "Monday"
# Num_days = 31
# week = { "mon" : 1, "tue" : 2, "wen" : 3, "thus" : 4, "fri" : 5, "sat" : 6, "sun" : 7}
# res = week["sun"] + Num_days
# print(int(res/7))

# sort the given array

# ls = [4,3,8,6,9,1,4,8]
# for i in range(len(ls)):
#     for j in range(len(ls)-i-1):
#         if ls[j] > ls[j+1]:
#             ls[j], ls[j+1] = ls[j+1] , ls[j]
# print(ls)
# this approach(Bubble sort) has more time complexcity n^2

# the below code is one of the way of insertion , it has also same time complexcity
# ls = [4,3,8,6,9,1,4,8]
# for i in range(len(ls)):
#     for j in range(i,len(ls)):
#         if ls[i] > ls[j]:
#             ls[i], ls[j] = ls[j], ls[i]

# print(ls)


# Given an integer array 'nums', return 'true' if any value appears at least twice in the array, 
# and return 'false' if every element is distinct.
# num = [1,2,3,1]
# def dupl(x):
#     if len(num) != len(set(num)):
#         print(True)
#     else:
#         print(False)
# dupl(num)


# find the freq of char in string

# name = "hello"
# cnt = {}
# for i in name:

#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1
# print(cnt)

# Find the frequency of each word in a sentence.

# line = "the cat sat on the mat the cat"
# freq = {}
# for i in line.split():
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)


# Find the character that appears the most in a string.

# line = "progrooooamming" 
# freq = {}
# # 1. Build the frequency dictionary (This part was good!)
# for i in line:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# # 2. Find the maximum
# max_char = ""
# max_count = 0

# for char, count in freq.items(): # Use .items() to get key and value
#     if count > max_count:        # Check if current count is bigger than the best so far
#         max_count = count        # Update the highest count
#         max_char = char          # Update the character that owns that count

# print("Max Character:", max_char)
# print("Max Count:", max_count)


# Remove duplicate characters keeping original order.

# line = "programming"
# seen = set()
# result  = ""
# for i in line:
#     if i not in seen:
#         result += i
#         seen.add(i)
# print(result)

# name =  "hello world"
# rev = name.split()
# result = []
# # print(rev)
# for i in rev:
#     result.append(rev[::-1])
# print(" ".join(result))

# line = "i love python"
# newline = line.split()
# result = reversed(newline)
# print(" ".join(result))

# Find the smallest number.

# num = [-4, -1, 3, -5, -7, -1]
# small = float("inf")
# for i in num:
#     if i < small:
#         small = i
# print(small)  # -7


# Remove duplicate characters keeping original order.
# i am solving it with different approaches

# line = "programming"
# seen = []
# for i in line:
#     if i not in seen:
#         seen.append(i)
# print(seen)

# line = "programming"
# result = ""
# for ch in line:
#     if ch not in result:
#         result += ch
# print(result)

# by above two approaches it gives O(n²) but following one gives o(n) becuase:
# 🔥 Why this is best:
# set lookup → O(1) (very fast)
# Overall time complexity → O(n)
# Clean + scalable

# s = "programming"
# seen = set()
# result = ""
# for ch in s:
#     if ch not in seen:
#         result += ch
#         seen.add(ch)
# print(result)

# Reverse the order of words in a sentence.
# Input: "I love Python" → Output: "Python love I"

# line = "hello world"
# words = line.split()
# rev = []

# for i in range(len(words), -1, -1):
#     rev.append(words[i])

# print(rev)

# To check Palindrom

# line = "racecar"
# i,j = 0,len(line)-1
# while i < j:
#     if line[i] != line[j]:
#         print("Not Palindrom")
#     i += 1
#     j -= 1
# else:
#     print("Palindrom")


# Return True if all characters in the string are unique.

# line = "abcde"
# res = {}
# for i in line:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

# for val in res.values():
#     if val > 1:
#         print(False)
#         break
# else:
#     print(True)

# Another Way:

# line = "asdff"
# if len(set(line)) == len(line):
#     print(True)
# else:
#     print(False)