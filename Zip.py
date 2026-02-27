# 🧠 What is zip() in Python?

# zip() function multiple iterables ko combine karta hai element-wise and ek iterator return karta hai.

names = ["A", "B", "C"]
marks = [90, 85, 88]

result = zip(names, marks)
print(list(result))

# 🚀 Real-Life Use Cases


# 1️⃣ Dictionary banana
keys = ["id", "name", "age"]
values = [101, "Siddesh", 23]

d = dict(zip(keys, values))

# 2️⃣ Parallel Iteration

names = ["A", "B", "C"]
marks = [90, 85, 88]
for name, mark in zip(names, marks):
    print(name, mark)

# 🧠 Unequal Length Example
a = [1, 2, 3]
b = [10, 20]
print(list(zip(a, b)))

# Output:
[(1, 10), (2, 20)]

# 👉 Shortest iterable tak hi combine karta hai.

# 3️⃣ ETL / Data Processing

# Two columns align karna
# Paired dataset process karna
# Mapping logic create karna


# The zip() function combines multiple iterables element-wise and returns an iterator of tuples.
# It is commonly used for parallel iteration and creating mappings like dictionaries.
