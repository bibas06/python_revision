import functools
nums=[2,3,4,5,6,7,8]
def func(a,b):
    return a+b
print(functools.reduce(func,nums))
#Output-sum(2,3,4,5,6,7,8)