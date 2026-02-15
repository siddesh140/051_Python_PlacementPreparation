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