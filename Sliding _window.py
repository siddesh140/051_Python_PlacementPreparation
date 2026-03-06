# The Sliding Window technique is a way to look at a "window" of a larger dataset (like a list or string) and
#  move that window over the data one step at a time.

# Instead of re-calculating everything inside the window from scratch, you only update the window by adding
#  the new element and removing the old one.

# The "Subway Sandwich" Analogy
# Imagine you are eating a giant 12-inch sub, but you can only see 3 inches of it through a small hole in a box.

# You see the first 3 inches.

# To see the next 3 inches, you don't throw the sub away and get a new one.

# You just slide the sub to the left. One inch disappears (the old part), and a new inch appears (the new part).

nums = [1, 2, 10, 4, 5, 6]
k = 3  # Window size

# 1. Get the sum of the first window
window_sum = sum(nums[:k])
max_sum = window_sum

# 2. "Slide" the window across the rest of the list
for i in range(len(nums) - k):
    # Subtract the element that's left behind, add the new element
    window_sum = window_sum - nums[i] + nums[i + k]
    max_sum = max(max_sum, window_sum)

print(max_sum) # Output: 19 (which is 10 + 4 + 5)

num = [1,2,3,4,5,6]
k = 3
window_sum = sum(num[:k])
for i in range(k,len(num)):
    window_sum = window_sum + num[i] - num[i-k]