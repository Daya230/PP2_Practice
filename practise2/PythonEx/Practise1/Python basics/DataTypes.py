#ex1
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 

'''
<memory at 0x14acabf365c0>
<class 'memoryview'>
'''

#ex2
x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
'''
bytearray(b'\x00\x00\x00\x00\x00')
<class 'bytearray'>
'''

#ex3
x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#ex4
x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

'''
{'name': 'John', 'age': 36}
<class 'dict'> 
'''

#ex5
x = complex(1j)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
'''
1j
<class 'complex'>
'''