from itertools import product #type: ignore in order to suppress warning
a=[1,2]
b=[3,4]
p=product(a,b)
prod=product(a,b,repeat=2)#repeatation is alloowed two times
print(list(prod))
print(list(p))