 1634
count = sum((int(i)**4 for i in str(num)))
if count == num:
    print("Its an Armstrong number")
else:
    print("Not Armstrong Number")