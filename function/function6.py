#default aguments on mutable datatypes
def add_items(name,data=[]):
    data.append(name)
    print("Updated data is :",data)#we are expecting:
add_items("bibas")                            #['bibas]
print(add_items.__defaults__)                 
add_items("biswas")                           #['biswas]
print(add_items.__defaults__)               
add_items("nikhil")                           #['nikhil]
print(add_items.__defaults__)               








