#ex1
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#ex2
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

print(type(x),type(y),type(z))

#ex3
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

""" give error
2myvar = "John"
my-var = "John"
my var = "John"
"""

#ex4 assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#ex5 
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#or
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#ex6
x = 5
y = "cat"
print(x, y)

#ex7 global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

#or

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

#ex8

x = "awesome" #присваивает значение

def myfunc():
  global x #обязательно надо инициализировать
  x = "fantastic" # при вызове функции будет менять это значение

myfunc()

print("Python is " + x) #на выходе получим измененное


