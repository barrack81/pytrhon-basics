#generators are functions that return an iterator
# they can pause and resume their execution
"""def my_generator():
    yield 1
    yield 2
    yield 3
for x in my_generator():
    print(x)

def gen_numbers(n):
    for i in range(n):
        yield i
        
for x in gen_numbers(5):
        print(x)


def count_up_to(n):
    count = 1
    while count <=  n:
        yield count
        count += 1
for x in count_up_to(5):
    print(x)"""
    


def simple_gen():
    yield "hello"
    yield "world"
    yield "!"
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))