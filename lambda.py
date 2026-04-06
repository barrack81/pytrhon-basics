#lambda is a function that takes a function as input and returns a new function
#lambda is used to create anonymous functions
"""add =lambda a, b : a + b #this means take a and b as input and return a + b
print(add(5, 9))

#this is the same as

def add(a, b):
    return a + b
print(add(5, 9))
def square(x): 
    return x * x
numbers = [1, 2, 3]
result = list(map(square, numbers))
print(result)

square = lambda x : x * x
numbers = [1, 2, 3]
result = list(map(square, numbers))
print(result)
def x (a):
    return a + 10
print(x(5))
def x (a, b):
    return a * b
print(x (5, 6))
x = lambda a, b : a * b
print(x(5, 6))
square = lambda x : x * x
number = [1, 2, 3]
result = []
for num in number:
    result.append(square(num))
print(result)

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
mytrippler = myfunc(3)

print(mydoubler(11))
print(mytrippler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

def double(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(double(num))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


numbers = [1, 2, 3, 4, 5, 6,]
def odd(x):
    return x % 2 !=0
odd_numbers = []
for num in numbers:
    if odd(num):
        odd_numbers.append(num)
print(odd_numbers)"""

students = [("Emil", 25), ("roy", 22),("Linus", 30)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
