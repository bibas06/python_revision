import sys
n1=int(input("enter the first number :"))
n2=int(input("enter the second number :"))
try:
    div=n1/n2
    print('the division is :',div)
except:
    print(sys.exc_info()[0])#gives the exception name i.e.<class 'error_name'>
    print(sys.exc_info()[1])#gives the exception information
    print(sys.exc_info())