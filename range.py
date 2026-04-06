#in python range is a function that returns a sequence of numbers
#range(start, stop, step)
"""x  = range(3, 10)
print(x)

for i in range(10):
    print(i) #output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 10, 2):
    print(i) # output [0, 2, 4, 6, 8]
    
print(list(range(10))) #output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(10)
print(r[2])#output = 2
print(r[:3]) #output = range(0, 3)
print(r[-3:]) #output = range(7, 10)"""

r = range(0, 10, 2)
print(11 in r) # output = False
print(6 not in r) #output = false
print(len(r))