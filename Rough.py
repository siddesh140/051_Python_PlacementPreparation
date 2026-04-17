# def check_anagram(s1,s2):
#     if len(s1) != len(S2):
#         return False
#     freq = {}

#     for char in s1:
#         freq[char] = freq.get(char,o) + 1

#     for char in s2:
#        if char not in freq or freq[char] == 0:
#             return False
#     freq[char] -= 1
#     return True
# alpha = "programming"
# s1 = ""
# s2 = ""
# for i in range(len(alpha)):
#     if (i+1) % 2 == 0 :
#         s1 += alpha[i]
#     else:
#         s2 += alpha[i]
# print(s1,s2)

# alpha = "programming"
# s1 = alpha[1::2]
# s2 = alpha[::1]
# print(s1,s2)

# li = [5,4,1,4,5,3,4,4,3,3]

# def duplicate(li):
#     seen = []
#     for i in li:
#         if i not in seen:
#             seen.append(i)
#     print(seen)

# duplicate(li)

# sorting

ls = [5, 6, 1, 0, 4, 8, 9]
# bubble sort
# for i in range(len(ls)):
#     for j in range(len(ls)):
#         if ls[i] < ls[j]:
#             ls[i], ls[j] = ls[j], ls[i]
# print(ls)

# insertion

# for i in range(len(ls)):
#     for j in range(i,len(ls)):
#         if ls[i] > ls[j]:
#              ls[i], ls[j] = ls[j], ls[i]

# print(ls)

# n= len(ls)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if ls[j] > ls[j+1]:
#             ls[j], ls[j+1] = ls[j+1], ls[j]
# print(ls)

# time = int(input())
# total_fare = 0

# if time < 0:
#     raise "value error"

# for i in range(1,time+1):
#     if i <= 2:
#         total_fare += 100
#     elif i >=3 and i <= 5:
#         total_fare +=50
#     else:
#         total_fare += 20

# print(total_fare)

# ls = [40,30,50,60]
# cp = 100

# ls1 = sorted(ls)
# sum1 =0
# cnt = 0
# for i in range(len(ls1)):
#     if cp > sum1:
#         sum1+=ls1[i]
#         cp -= ls1[i]
#         cnt+= 1

# print(cnt)
# print(ls1[:cnt])

# ls = [5,7,4,9,8,1,2]

# for i in range(len(ls)):
#     for j in range(len(ls)-i-1):
#         if ls[j] > ls[j+1]:
#             ls[j], ls[j+1] = ls[j+1] , ls[j]
# print(ls)

# Factorial

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     return fact
# fact(5)

# name = "mango"
# # name1 = name[::-1]
# # print(name1)
# rev = ""

# for i in name:
#     rev = i + rev
# print(rev)

# num = 12345
# temp = num
# total = 0
# while num > 0:
#     digit = num % 10
#     total = total * 10  + digit
#     num = num // 10
# print(total)

# s = "hhsseuffhshhriiii"

# ch = {}

# for i in s:
#     if i in ch:
#         ch[i] += 1
#     else:
#         ch[i] = 1
# print(ch)

# num = 5

# a,b = 0,1
# while True:
#     a ,b = b , a+b
#     if a >= 5 and a <=  15:
#         print(a)
#     if a > 15:
#         break


# num = 153
# one = 0
# new_num = str(num)
# for i in new_num:
#     one += int(i)**len(new_num)
# print(one)
# if one == num:
#     print(True)

# num = [4,3,4,1,1,4,3]
# seen = {}
# for i in num:
#     seen[i] += 1
# print(seen.values)

# num = [4, 3, 6, 5, 7, 9]
# # large = max(num)
# # max1 = 0
# # for i in num:
# #     if i > max1 and i < large:
# #         max1 = i
# # print(max1)
# new = sorted(num)
# print(new[::-1][1])

# def fact(x):
#     fact = fact * x
#     return fact

# v = 45
# total = 0
# while v > 0:
#     digit  = v % 10
#     total = total + fact(digit)
#     v = v // 10
# print(total)


# num = 1634
# count = sum((int(i)**4 for i in str(num)))
# if count == num:
#     print("Its an Armstrong number")
# else:
#     print("Not Armstrong Num")

# name = "qwertyui"
# cnt = 0
# for i in name:
#     cnt += 1
# print(cnt)

# line = "I love Java Programming"
# cnt = 0
# for i in line:
#     if i != " ":
#         cnt += 1
# print(cnt)

# num = [2,5,4,3,6,7,5,4,4]
# # result = sorted(set(num))[-2]
# # print(result)

# large = max(num)
# second = 0
# for i in num:

#     if i > second and i < large:
#         second = i
# print(second)

# name1 = "bring"
# name2 = "grinb"
# if len(name1) != len(name2):
#     print(False)
#     # By using sorted
# if sorted(name1) == sorted(name2):
#     print("Anagram")
#     # by importing collection

# from collections import Counter

# if Counter(name1) == Counter(name2):
#     print("Anagram")

# # Given an integer array 'nums', return 'true' if any value appears at least twice in the array,
# # and return 'false' if every element is distinct.
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
# # result = ""
# newline = line.split()
# # for i in newline:
# #     result.append(i)[::-1]
# # print(" ".join(result))

# result = reversed(newline)
# print(" ".join(result))

# check palindrom

# name = "Malayalam"
# if name.lower() == name[::-1].lower():
#     print("pal")

# Usin Two Pointer Technique

# name = "Malayalam"
# i,j = 0, len(name)-1
# is_pal = True
# while i < j:
#     if name[i].lower() != name[j].lower():
#         is_pal = False
#     i += 1
#     j -= 1
# print(is_pal)


# num = 12345
# a,b = 0,1
# while a < num:
#     print(a, end=" ")
#     a,b = b, a+b

# num = 10
# count = 0
# a, b = 0, 1

# while count <  num:
#     print(a, end=" ")
#     # The magic line: a becomes b, and b becomes the sum of both
#     a, b = b, a + b
#     count += 1

# name = "hello"
# cnt = {}
# for i in name:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1
# print(cnt)

# find smallest number

# num = [-4, -1, 3, -5, -7, -1]
# small = float("inf")
# for i in num:
#     if i < small:
#         small = i
# print(small)  # -7

# greet = "hello"
# freq = {}
# for i in greet:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)

# Input = "the cat sat on the mat the cat"
# # count = Input.split()
# freq = {}
# large = 0
# max_char = ""
# for i in Input:
#     if i != " ":
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
# for j in freq:
#     if freq[j] > large:
#         large = freq[j]
#         max_char = j
# print(freq)
# print(f"most frequent charecter {max_char} with frequency {large}")


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

# line = "enodesrever"
# rev = ""
# for i in line:
#     rev = i + rev
# print(rev)

# line = "hello world"
# rev = ""
# for i in line.split():
#     for j in i:
#         rev = j + rev
# print(rev)

# line = "hello world"
# words = line.split()
# rev = []

# for i in range(len(words), -1, -1):
#     rev.append(words[i])

# print(rev)

line = "racecar"
# res = ""
# for ch in line:
#     res = ch + res 
# if line == res:
#     print(True)
# line = "racecar"
# i,j = 0,len(line)-1
# while i < j:
#     if line[i] != line[j]:
#         print("Not Palindrom")
#     i += 1
#     j -= 1
# else:
#     print("Palindrom")

# line1 = "Listen"
# line2 = "Silent"

# if len(line1) == len(line2):
#     if sorted(line1) == sorted(line2):
#         print("ANagram")
#     else:
#         print("Not ANagram")
