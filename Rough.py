# Jack loves Sundays. He wants to find out how many Sundays will occur in a month if he knows two things:
# - The day on which the month starts (e.g., Monday, Tuesday, etc.)
# - The total number of days in that month
# Your task is to determine how many Sundays fall in that month based on this information.

# month_start = "Monday"
# Num_days = 31
# week = { "mon" : 1, "tue" : 2, "wen" : 3, "thus" : 4, "fri" : 5, "sat" : 6, "sun" : 7}
# res = week["sun"] + Num_days
# print(int(res/7))

# num = 8
# num1 = (1 << num.bit_length()) - 1
# print(num ^ num1)

# 2 4 8 16
# 1 2 4 8 
# 0 1 2 3 4 
# 2 2 2 2 2

# 1 1 1 = 7
# 0 0 0 = 0

num = 5
li = [0,0,1,0,2,1,2,0]
zero = 0
one = 0
two = len(li)-1
while one <= two:
    if li[one] == 0:
        li[zero], li[one] = li[one], li[zero]
        zero += 1 
        one += 1
    elif li[one] == 1:
        one += 1
    else :
        li[one], li[two] = li[two], li[one]
        two -= 1
print(li)


    


