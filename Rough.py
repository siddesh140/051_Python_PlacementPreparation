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

ls = [5,6,1,0,4,8,9]
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

ls = [5,7,4,9,8,1,2]

for i in range(len(ls)):
    for j in range(len(ls)-i-1):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1] , ls[j]
print(ls)





