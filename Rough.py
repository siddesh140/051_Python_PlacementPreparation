name = "Nayan"
# rev = ""
# for i in name:
#     rev = i.lower() + rev
# if rev == name.lower():
#     print(True)
# else :
#     print(False)

left = 0
right = len(name)-1
flag = False
while left < right :
    if name[left].lower() != name[right].lower():
        flag = False
        break
    else:
        left += 1
        right -= 1
        flag = True

print(flag)