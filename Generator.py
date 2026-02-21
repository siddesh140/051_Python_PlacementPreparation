# What is yield?

# yield is a keyword in Python used to create a generator. It allows a function to return a value while saving its state,
# so it can resume execution from the same point later.

# 📦 Normal Function vs Generator
# Normal Function
def normal():
    return 1

# Returns once
# Execution stops
# Memory freed

# Generator Function
def gen():
    yield 1

# Does NOT execute immediately
# Returns a generator object
# Execution pauses at yield
# Resumes from same point

# 🔥 How yield Works Internally

# Example:

def count():
    print("Start")
    yield 1
    yield 2
    yield 3

g = count()

print(next(g))
print(next(g))
# What happens?

# Function does NOT run at definition
# Runs only when next() is called
# Stops at each yield
# Remembers where it stopped
# This memory of state = key feature.

# ----------------------------------------

# 🚀 What is a Generator?

# A generator is a function that produces a sequence of values lazily using yield, instead of returning them all at once.
# Lazy = value generate only when needed

# 🎯 Now the Important Part

# Why Generators Preferred Over Lists in ETL Pipelines?
# This is where you impress interviewer.

# 1️⃣ Memory Efficiency (Most Important)

# List:

data = [x for x in range(10_000_000)]

# Entire data stored in memory
# Heavy memory usage

# Generator:

data = (x for x in range(10_000_000))

# Generates one value at a time
# Does NOT store all values
# Very low memory usage

# 2️⃣ Streaming Data Handling

# 3️⃣ Faster Startup

# List:

# Takes time to build full structure first

# Generator:

# Starts processing immediately
# Very useful in pipelines.

# 🔥 Interview-Ready Answer

# You can say:

# Yield is used to create generators in Python. Unlike a normal function that returns a value and exits,
# a generator function pauses execution at each yield statement and resumes from the same point when called again.
# Generators are preferred in ETL pipelines because they are memory-efficient and process data lazily, which is crucial when handling large datasets.
# Instead of loading entire data into memory like lists, generators produce one item at a time, making them scalable and suitable
# for streaming and big data applications.


# How to call Generator ?

def func():
    yield 10
    yield 13
    print("Hello")

print(func())

# there are two ways to call generator :

# By using next()
g = func()
print(next(g))
print(next(g))

print("------")
# By using Loop

for i in func():
    print(i)

