# a = [1,2,3]
# b = 2 * a
# print(b)
# a = [[1]] * 3
# a[0] = 99
# print(a)
import copy

# a = [1,2,[3]]
# b = copy.deepcopy(a)
# b.append(4)

# print(a)
# print(b)

# a = [[1], {2}, 3]
# b = copy.copy(a)
# b[0][0] = 99

# print(a)
# print(b)

# a = [1,2,3]
# print(a[::-2])

# a = [1,2,3]
# b = a
# b.append(4)
# print(a)

# import copy
# import time

# # Large nested structure
# data = [[i for i in range(1000)] for _ in range(1000)]

# # Shallow copy - FASTER ⚡
# start = time.time()
# shallow = copy.copy(data)
# print(f"Shallow: {time.time() - start}")  # ~0.0001 seconds

# # Deep copy - SLOWER 🐢
# start = time.time()
# deep = copy.deepcopy(data)
# print(f"Deep: {time.time() - start}")     # ~0.5 seconds

# Dictionaries use hash values to find values quickly (O(1))
person = {'name': 'Alice', 'age': 25}

# When you do person['name'], Python:
# 1. Calculates hash of 'name'
# 2. Uses that hash to find the value instantly

print(hash('name'))  # Output: -8835372099674341033 (consistent)
print(hash('age'))  # Output: -8835372099674341033 (consistent)