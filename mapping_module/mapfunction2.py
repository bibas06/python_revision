marks=[10,20,30,40,50]
def logic(arg1):
    return arg1+1
mapped_obj=map(logic,marks)
for i in mapped_obj:
    print(i)
print(type(mapped_obj))
list=[1,2,3,4,5,6,7,8,9]
def even_odd(arg1):
    if arg1%2==0:
        return arg1
filter_obj=filter(even_odd,list)
for i in filter_obj:
    print(i)
print(type(filter_obj))