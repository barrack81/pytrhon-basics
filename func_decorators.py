# decoratos are functions that add functionality to other functions
# decorator functions are used to modify the behaviour of other functions
# a decorator is a function that takes another function as input and returns an new function


def greet():
    print("good morning")


def decorator(func):
    def wrapper():
        print("hello")
        func()
        print("have a nice day")

    return wrapper


@decorator
def greet():
    print("good morning")


greet()
