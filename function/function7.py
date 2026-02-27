#variable-length in positional arguments
def add(*nums):
    sum=0
    print(nums)
    for i in nums:
        sum+=i
    return sum
a=add(10,20,30)
print(a)
print(add(10,20))
print(add(10,20,30,40))
#variable length in keyword arguments
def add2(**nums):
    print(nums)
    return sum(nums.values())
print(add2(n1=10,n2=20,n3=30))
print(add2(n1=10,n2=20))
print(add2(n1=10,n2=20,n3=30,n4=40))
#P.A-->Variblelength P.A-->K.A-->Variablelength K.A-->D.A
