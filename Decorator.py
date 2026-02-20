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