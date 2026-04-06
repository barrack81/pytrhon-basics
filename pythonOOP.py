# Object oriented programming (OOP)
# OOP is a programming paradigm that uses objects and their interactions to model real-world entities
# OOP is a way of structuring code to make it easier to understand and maintain
#classes are templates for creating objects
#objects are instances of classes
#methods are functions that belong to a class
#attributes are variables that belong to a class
#inheritance is a way of creating new classes that are based on existing classes
#polymorphism is a way of writing code that can work with different types of objects
#encapsulation is a way of hiding the implementation details of a class
#abstraction is a way of hiding the implementation details of a class

"""class car: #this is a class
    color = "red" #this is an attribute
my_car = car() #this is an object
print(my_car.color) #this is a method

class roy: #this creates a class
    age = 25 # this is an attribute.it simulates a variable
describe = roy() #this is an object which means creates an instance called describe from the class roy
print(describe.age)# this is a method. it simply means print the value of the attribute age by using the object describe


class simulate: # this is a class
    def greet(self): # this is a method
        print("good morning") #

sim = simulate()# this is an object
print(sim.greet())# this is a method
#the parameter self in function greet is a placeholder for the object that is calling the method

class person:
    def greet(self):
        print("good morning")

roy = person()
mary = person()

roy.greet()
mary.greet()

class Person:
    def __init__(self, name):
        self.name = name# this is an attribute
        
    def greet(self):
        print("hello " + self.name)
        
roy = Person("roy")
mary = Person("mary")# this is an object

roy.greet()
mary.greet()

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hello, my name is {self.name} and i'm {self.age} years old")

roy = Person("Roy", 22)        
print(roy.name)
print(roy.age)
roy.greet()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(self.name + " says woof!")

d1 = Dog("Buddy", 3)
d1.bark()

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hello, my name is {self.name} and i'm {self.age} years old")
        
    def birthday(self):
        self.age += 1
        
    def introduce(self):
        print(f"hi my name is {self.name}")

roy = Person("Roy", 22)  
mary = Person("Mary", 20)
James = Person("James", 25)
      
roy.greet()
mary.greet()
James.greet()

roy.birthday()
mary.birthday()
James.birthday()

roy.greet()
mary.greet()
James.greet()

class Car:
    def __init__ (self, brand):
        self.brand = brand
    def show(self):
        print(self.brand)
c1 = Car("Ford")
c1.show()

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello, my name is {self.name} and i'm {self.age} years old")
        
    def birthday(self):
        self.age += 1
        
        
        
    def introduce(self):
        print(f"hi my name is {self.name}")
        
    def with_a(self):
        new_list = []
        if "a" in self.name.lower():
            new_list.append(self.name)
        return new_list
        
    
        

roy = Person("Roy", 22)  
mary = Person("Mary", 20)
James = Person("James", 25)

people = [roy, mary, James]

result = []

for person in people:
    if person.with_a():
        result.append(person.name)
        
print(result)

roy.greet()
mary.greet()
James.greet()

roy.greet()
mary.greet()
James.greet()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(f"hello my name is {p1.name} and i'm {p1.age} years old")


class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
car1 = Car("Ford", "Mustang")

del car1.model
#this condition will print an output if it cant find model of the car
if "model" in car1.__dict__:
    print("yes")
else:
    print("no")
    
class Student:
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna", "A")
print(s1.grade)
#change the grade to B
s1.grade = "B"
print(s1.grade)
    

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
calc = Calculator()
print(calc.add(5, 6))
print(calc.multiply(5, 6))


class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def __str__ (self):
        return f"{self.name} ({self.age})"

p1 = Person("John", 36)
print(p1)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
        print(f"added {song}")
        
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"removed {song}")
        else:
            print(f"{song} not found in playlist")
    
    def show_songs(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"- {song}")

playlist = Playlist("My Playlist")
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")
playlist.remove_song("Song 2")
playlist.show_songs()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def Area(self):
        return self.width * self.height
    
r1 = Rectangle(5, 3)
print(r1.Area())

class Person:
    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def greet(self):
        return f"hello my name is {self.fname} {self.lname}"

x = Person("Roy", "Barrack")
print(x.greet())
--------------------------------------------------------------------------
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def move(self):
        return f"{self.make} {self.model} is moving"
    
class Car(Vehicle):
    pass

c1 = Car("Ford", "Mustang", 2022)
print(c1.move())

------------------------------------------------------------------------------

class Vehilcle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def move(self):
        return f"{self.make} {self.model} is moving"
    
class Car(Vehilcle):
    def honk(self):
        return f"{self.make} {self.model} is honking"
    
c1 = Car("Ford", "Mustang", 2022)
print(c1.move())
print(c1.honk())

------------------------------------------------------------


class Vehicle:
    def move(self):
        print("moving")
        
class Car(Vehicle):
    def move(self): # this is method overiding
        print("the car is driving")
        
c1 = Car()
c1.move()

---------------------------------------------------------------------

class Road_user:
    def __init__ (self, name):
        self.name = name
    
    def obey_rules(self):
        print(f"{self.name} should follow traffic rules")
        

class Driver(Road_user):
    def drive(self):
        print(f"{self.name} is driving")
        
class Pedestrian(Road_user):
    def walk(self):
        print(f"{self.name} is walking")
        
d1 = Driver("Roy")
d1.obey_rules()
d1.drive()

p1 = Pedestrian("Stella")
p1.obey_rules()
p1.walk()

--------------------------------------------------------------------

class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        
    def work(self):
        return f"{self.name} is working and his salary is {self.salary}"
    

class DataAnalyst(Employee):
    def analyze_data(self):
        return f"{self.name} is a data analyst here"
    


class Manager(Employee):
    def manage_team(self):
        return f"{self.name} works here as the managing director"


e1 = Employee("Roy", 50000)
print(e1.work())

da1 = DataAnalyst("Stella", 60000)
print(da1.work())
print(da1.analyze_data())

da2 = Manager("Barrack", 1000000)
print(da2.work())
print (da2.manage_team())

class Car:
    def __init__ (self, make, model):
        self.make = make
        self.model = model

class Mercedes(Car):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color
        

class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        return f"{self.name} is working and his salary is {self.salary}"

class DataAnalyst(Employee):
    def __init__(self, name, salary, tools):
        super().__init__(name, salary)
        self.tools = tools
        
    def analyze_data(self):
            return f"{self.name} uses {self.tools} to analyze data 📊"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__ (name, salary)
        self.department = department
        
    def manage_team(self):
        return f"{self.name} is a manager in the {self.department} department"



da1 = DataAnalyst("Barrack Roy", 1000000, "Python")
print(da1.work())
print(da1.analyze_data())

da2 = Manager("Silverstone", 2000000, "IT")
print(da2.work())
print(da2.manage_team())



#lets do encapsulation+
#encapsulation means hiding internal data and controlling how it is accessed

class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.__salary = salary #this is a private attribute
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("salary must be greater than 0")
            
    def work(self):
        return f"{self.name} is working and his salary is {self.__salary}"

class DataAnalyst(Employee):
    def __init__ (self, name, salary, tools):
        super().__init__(name, salary)
        self.tools = tools
    def analyze_data(self):
        return f"{self.name} uses {self.tools} to analyze data 📊"

class Manager(Employee):
    def __init__(self,name, salary, department = "IT"):
        super().__init__(name, salary)
        self.department = department
        
    def increase_salary(self, amount):
        if amount > 0:
            new_salary = self.get_salary() + amount
            self.set_salary(new_salary)
        else:
            print("amount must be greater than 0")
            
class Director(Employee):
    def __init__ (self, name, salary, department = "IT"):
        super().__init__(name, salary)
        self.department = department
        
    def increase_salary(self, amount):
        if amount > 0:
            new_salary = self.get_salary() + amount
            self.set_salary(new_salary)
        else:
            print("amount must be greater than 0")
            
class Intern(DataAnalyst):
    def __init__(self, name, salary, tools, duration):
        super().__init__(name, salary, tools)
        self.duration = duration
        
    def learn(self):
        return f"{self.name} is learning {self.tools} for {self.duration} hours"
            

e1 = Employee("Roy", 50000)
print(e1.get_salary())
e1.set_salary(60000)
print(e1.get_salary())
e1.set_salary(-50000)
print(e1.work())

da1 = DataAnalyst("Barrack", 1000000, "Python")
print(da1.work())
print(da1.analyze_data())

da2 = Manager("Silverstone", 2000000)
print(da2.work())
da2.increase_salary(50000)
print(da2.work())

da3 = Director("Barrack", 1000000)
print(da3.work())
da3.increase_salary(50000)
print(da3.work())

da4 = Intern("Martin", 1000000, "Python", 10)
print(da4.work())
print(da4.learn())

class Cat:
    def sound(self):
        print("Meow")
        
class Fox:
    def sound(self):
        print("wa-pa-pa-pa-pa-pow!")
        
c1 = Cat()
f1 = Fox()
for animal in (c1, f1):
    animal.sound()
    
    
class Scoreboard:
    def __init__ (self, score):
        self.__score = score
        
    def get_score(self):
        return self.__score
s1 = Scoreboard(0)
print(s1.get_score())


----------------------------------------------------------------------------
class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("salary must be greater than 0")
            
    def work(self):
        return f"{self.name} is working and his salary is {self.__salary}"
    
    
class DataAnalyst(Employee):
    def __init__ (self, name, salary, tools):
        super(). __init__(name, salary)
        self.tools = tools
    
    def work(self):
        return f"{self.name} is analyzing data with {self.tools}"
    
    
class RoadSafetyOfficer(Employee):
    def __init__ (self, name, salary, region):
        super(). __init__(name, salary)
        self.region = region
    
    def work(self):
        return f"{self.name} is working in the {self.region} region"
        


class Manager(Employee):
    def __init__ (self, name , salary, department):
        super(). __init__(name, salary)
        self.department = department
        
    
    def increase_salary(self, amount):
        if amount > 0:
            new_salary = self.get_salary() + amount
            self.set_salary(new_salary)
        else:
            raise ValueError("amount must be greater than 0")
        
    def work(self):
        return f"{self.name} is managing the {self.department} department."
        
staff = [
    DataAnalyst("Roy", 50000, "Python"),
    Manager("Barrack", -1000000, "Operations"),
    RoadSafetyOfficer("Seth", 1000000, "London")
]

for everyone in staff:
    print(everyone.work())"""
    
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__ (self, name, salary):
        self.name = name
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("salary must be greater than 0")
            
    @abstractmethod
    def work(self):
        pass
    
class DataAnalyst(Employee):
    def __init__ (self, name, salary, tools):
        super().__init__(name, salary)
        self.tools = tools
        
    def work(self):
        return f"{self.name} is analyzing data with {self.tools}"

class Manager(Employee):
    def __init__ (self,name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def work(self):
        return f"{self.name} is managing the {self.department} department"
    
    def increase_salary(self, amount):
        if amount > 0:
            new_salary = self.get_salary() + amount
            self.set_salary(new_salary)
        else:
            raise ValueError("amount must be greater than 0")
     
#Intern takes the properties of Data Analyst, this is multilevel inheritance
        
class Intern(DataAnalyst):
    def __init__(self, name, salary, tools, duration):
        super(). __init__(name, salary, tools)
        self.duration = duration
        
    def work(self):
        return f"{self.name} is analyzing data with {self.tools} for {self.duration} hours"

class Director(Manager):
    def work(self):
        return f"{self.name} is earning {self.get_salary()} as a director   "

staff = [
    DataAnalyst("Roy", 50000, "Python"),
    Manager("Barrack", -1000000, "Operations"),
    Intern("Stella", 30000, "Python", 4),
    Director("Seth", 1000000, "Operations")
]

for people in staff:
    print(people.work())