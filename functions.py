"""def my_function(*args):
  print("This is type", type(args))
  print("this is the first item on the list:", args[0])
  print("this is the second item on the list:", args[1])
  print("this is all the arguments:", args)
  for cont in args:
    if "a"in cont:
      print(f"theres an a in this: {cont}")
    else:
      print(f"nothing to show in: {cont}")
my_function("python", "is", "fun", "to", "learn", "yo", "should", "try", "it")


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello","Roy", "Stella", "Linus")

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
this_total = my_function(1,2,3,4)
print(this_total)


def my_function(**student):
    print("this is the type", type(student))
    print("good morning,", student["name"])
    print("it's an honor to present ot you this,", student["gift"])
    print("you're such an increadible person to work with", student["message"])
    print("all data", student)


my_function(name="Roy", gift=1000, message="Bravo")
x = 200
def my_function():
  x = 500
  print(x)
my_function()
print(x)
x = 300
def my_function():
  global x
  x = 200
my_function()
print(x)
def my_function1():
  x = "Jane"
  def my_function2():
    nonlocal x
    x = "hello"
  my_function2()
  return x
print(my_function1())

x = 300
def my_function():
  
  x = 200
my_function()
print(x)"""
