# 🐍 What is a Python Decorator?
# 🎯 Simple Definition (Interview Safe)

# A Python decorator is a function that takes another function as input, adds some additional functionality to it, and returns a new modified function — without changing the original function’s code.


def decorator_func(original_func):
    def wrapper():
        print("Before function execution")
        original_func()
        print("After function execution")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()


# 🧩 What @decorator Actually Does?

# @decorator_func
# def say_hello():

    # Is internally equal to:

# say_hello = decorator_func(say_hello)

# 🎯 Real-Life Use Cases

# Decorators are used for:
# Logging
# Authentication
# Access control
# Timing execution
# Caching
# Validation

# What is the difference between a decorator and a closure?

# A closure is a function that remembers the variables from its outer (enclosing) function even after the outer function has finished execution.

def outer():
    x = 10
    def inner():
        print(x)
    return inner

func = outer()
func()

# A decorator is a function that takes another function as input, adds extra functionality, and returns a modified function.

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

# 👉 Every decorator uses closure internally.
# 👉 But every closure is NOT a decorator.


# A closure is a function that retains access to variables from its enclosing scope even after the outer function completes. A decorator, on the other hand, is a design pattern that uses closures to modify or extend the behavior of another function without changing its code.

# 🔥 Important Interview Rule

# Closure = about remembering variables
# Decorator = about modifying functions