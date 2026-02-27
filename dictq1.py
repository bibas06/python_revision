student={"name" :"bibas","subjects" :{"maths" :99,"phy" :98,"chem":97}}
print(student.keys())
print(list(student.keys()))
print(student.items())#returns in tuple (key,value) pair
print(list(student.items()))
print(student["name"])#gives an error if key is not present
print(student.get("name"))#does'nt gives an error and returns None
new_dict={"city" :"jajpur","age":14}
student.update(new_dict)
print(student)
del student["age"]
print(student)