def even_or_odd(num):
    if num%2==0:
        return "the number {} is even".format(num)#f-strings
    else:
        return "the number {} is odd".format(num)
l=[1,2,3,4,5,6,7,8,9,16]
print(list(map(even_or_odd,l)))    
