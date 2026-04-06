# a try except block is used to catch and handle exceptions
# a try block is used to test a block of code for errors
# an except block is used to handle the error
# an else block is used to define a block of code to be executed if there is no error
# a finally block is used to define a block of code to be executed regardless of the result of the try and except blocks
"""try:
    print(x)
except:
    print("an exception occurred")
else:
    print("nothing went wrong")
finally:
    print("the try except is finished")
    
    
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("something went wrong when writting to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")

try:
    x = int(input("Enter a number: "))
    print(x)
except:
    print("an exception occurred")
else:
    print("nothing went wrong")
finally:
    print("the try except is finished")"""
    
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("nothing went wrong")
finally:
    print("the try except is finished")