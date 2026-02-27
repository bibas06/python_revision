import sys
try:
    age=int(input('enter your valid age :'))
    if age<0:
        print("invalid age")
    else:    
        print("your age is :",age)
except ValueError as err:
    print(sys.exc_info())
    print(err)
 