add=lambda x:lambda y:x+y#nested lambda function
func=add(10)
print(func(20))
square=lambda x:x**2
square_add=lambda func:lambda num :func(num)+num
"""var=square_add(square)
print(var(4))"""
#or
print(square_add(square)(4))