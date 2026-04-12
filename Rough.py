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

v = 12345
total = 0
while v > 0:
    digit  = v % 10
    total = total * 10 + digit
    v = v // 10
print(total)

