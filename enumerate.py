marks=[12,56,32,98,12,45,1,4]
''''index=0
for mark in marks:
    print(mark)
    if(index==3):
        print('harry , awesome!')
    index+=1
#Linting is a process to identifying bugs and stylist errors in our code.'''
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print('harry , awesome!')
'''The enumerate() function in Python adds a counter to an iterable and returns it as an enumerate
object (an iterator). It is commonly used in loops to track both the index and the value of items
during iteration.
iterable: Any object that supports iteration (e.g., list, tuple, string).
start (optional): The starting value for the counter (default is 0).
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(index, value)
output:
0 apple
1 banana
2 cherry
for index, value in enumerate(fruits, start=1):
    print(index, value)
output:
1 apple
2 banana
3 cherry'''