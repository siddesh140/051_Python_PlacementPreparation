# enumerate() function in Python is used to loop over an iterable and get both the index and
# the element at the same time. It returns an enumerate object that produces pairs in the
# form (index, element). This removes the need to manually maintain a counter variable during iteration.

# Syntax :   enumerate(iterable, start=0)
# Parameters:

# iterable: sequence or collection to iterate over.
# start (optional): starting value of the index. Default is 0.

# Return: Returns an enumerate object that generates (index, element) pairs.

# Examples

# Example 1: This code converts the enumerate object into a list of tuples.
# Each tuple contains the index and corresponding element from the list.

a = ["A", "B", "C"]
r = list(enumerate(a))
print(r)

# Output
[(0, "A"), (1, "B"), (2, "C")]
# Explanation: list(enumerate(a)) converts index-element pairs into a list of tuples.


# Example 2: This code starts the index from 1 instead of default 0 using the start parameter.

a = ["red", "green", "blue"]
for i, v in enumerate(a, 1):
    print(i, v)

# Output
# 1 red
# 2 green
# 3 blue

# Explanation: enumerate(a, 1) starts counting from 1.

# Example 3: This code retrieves elements one by one using next() on enumerate object.


a = ["x", "y", "z"]
e = enumerate(a)

print(next(e))
print(next(e))

# Output
(0, "x")
(1, "y")
# Explanation: next(e) returns the next (index, element) pair.

# Example 4: This code enumerates dictionary items and provides index with key-value pairs.

d = {"a": 10, "b": 20}
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)

# Output
# 0 a 10
# 1 b 20

# Explanation: enumerate(d.items()) returns index with (key, value) pairs.
