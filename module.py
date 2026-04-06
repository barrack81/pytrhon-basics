"""person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

import module as mx

a = mx.person1["age"]
print(a)

import platform
x = dir(platform)
print(x)"""

def greeting(name):
    print("hello " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

from module import person1

a = person1["age"]
print(a)