add=lambda a,b:a+b
print(add(12,34))#annonymous function i.e. no name function
#works faster than normal function and useful for only single line code
n=lambda a:a%2==0
print(n(23))
print(type(n))
x=lambda a,b:print("hello world")
print(x(10,29))
#you cannot return multiple statements in lambda function
add=lambda x,y:(x+y,x-y)#u can return multiple statements using tuple 
print(add(10,4))
#important
add=(lambda a,b:a+b)(3,4)
print(add)