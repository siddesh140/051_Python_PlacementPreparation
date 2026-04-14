num = [0, 1, 2, 0, 3, 4]
first = 0
for second in range(len(num)):
    if num[second] != 0:
        num[first], num[second] = num[second], num[first]
        first += 1

print(num)