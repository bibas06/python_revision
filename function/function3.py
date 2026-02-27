num=10
def display():
    global num #not specifying the variable num globally will result in
    num=num+4  #UnboundLocalError
    print(num)
display()
print(num) 
