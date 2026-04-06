#iterators are objects that can be iterated over
#iterators are objects that can be used to iterate over a sequence of values
"""my_tuple = ("apple", "banana", "cherry")
myit = iter(my_tuple)

print(next(myit))
print(next(myit))
print(next(myit)) #output = apple banana cherry

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))# output = b a n a n a


my_tuple = ("apple", "banana", "cherry")
mystr = my_tuple

for x in mystr:
    print(x)

class MyIterator:
    def __init__(self):
        self.x = 2 #this line means x = 2
        
    def __iter__(self):
        return self #this line means return self which is the object that is being iterated over
    
    def __next__(self):
        if self.x <= 6:
            val = self.x
            self.x += 2
            return val
        else:
            raise StopIteration
myiter = MyIterator()
for x in myiter:
    print(x)
    

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))"""

class myiter():
    def __init__(self):
        self.a = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

daro = myiter()
for x in daro:
    print(x)
