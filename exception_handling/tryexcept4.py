class FiveDivisionError(Exception):
    pass
try:
    n1=int(input("enter the first number :"))
    n2=int(input("enter the second number :"))
    if n2==5:
        raise FiveDivisionError("cannot divide by 5")
    div=n1/n2
    print("division is:",div)
except Exception as err:#or(FiveDivisionError,ZeroDivisionError) as err
    print(err)
    #an exceptiom can be raised forcefully
    #in python using the raise keyword