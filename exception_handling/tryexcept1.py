try:
    n=int(input("enter a number :"))
    value=10/n
    print(n)
except ZeroDivisionError as err1:#storing the error as a variable
    print(err1)
except ValueError as err2:
    print(err2)
#Syntax:
"""try:
    code containing exceptions(suspicious code)
except [exception name:]
    code to handle exception(if occured)
else:
    code to excute if no exception are there
finally:
    always executed"""