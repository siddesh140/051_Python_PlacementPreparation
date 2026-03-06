def sum(arr, target):
    left, right = 0, len(arr)-1

    while left < right :
        sum = arr[left]  + arr[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
#if no pair is found        
    return False

arr = [2,4,3,5,6,4]
target = 10

print(sum(arr,target))