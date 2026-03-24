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

alpha = "programming"
s1 = alpha[1::2]
s2 = alpha[::1]
print(s1,s2)






    





