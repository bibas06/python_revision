from itertools import permutations # type: ignore
from itertools import combinations,combinations_with_replacement # type: ignore
a=[1,2,3,4]
perm=permutations(a,2)#returns tuples elements of specified length 2
com=combinations(a,2)
com_wr=combinations_with_replacement(a,2)
print(list(com))
print(list(com_wr))
print(list(perm))