# Tuples are generally faster than lists because tuples are immutable, which makes them more memory-efficient
# and slightly optimized internally in Python.

# 🔥 Why Tuple Is Faster?
# 1️⃣ Immutability

# Tuple change nahi ho sakta.
# List change ho sakti hai.
# Because tuple is immutable:
# No need to track dynamic resizing
# No need to manage extra memory for append/remove
# Internally simpler structure
# Less overhead = faster access.

import sys

l = [1, 2, 3]
t = (1, 2, 3)
print(sys.getsizeof(l))
print(sys.getsizeof(t))

# Since tuples are immutable, Python can optimize them at the bytecode level, whereas lists require
# additional dynamic memory management, making tuples slightly faster in certain operations.
