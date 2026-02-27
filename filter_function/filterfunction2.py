str=input('enter a given string :')
l=list(str)
print(list(filter(lambda word:word if word in ('a','e','i','o','u') else None,l)))

