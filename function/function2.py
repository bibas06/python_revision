#local variable-the variale which is declared within a function 
#global variable-the variable which is declared outside the function
num=10#global variable
def display():
    num=20#local variable  L.V.>G.V. inside a function 
    print("inside",num)
display()
print("outside",num)
print(globals())