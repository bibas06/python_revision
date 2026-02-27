set={9,9.0}
print(set)#python treats 9 and 9.0 same when storing in a set
s={"9.0",9}
print(s)
"""
values={
("float",9.0),
("int",9) using built-in data types
}"""
s1={1,2,34,5,67,8}
s2={1,2,44,55,66,76}
print(s1-s2)
print(s1|s2)
print(s1&s2)
print(s1 ^ s2)