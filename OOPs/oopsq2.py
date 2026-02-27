class Student:
    college_name="nit durgapur"#class attributes
    def __init__(self,name,marks) -> None:
        self.name=name#object attributes      O.A.>>C.A. inside a function
        self.marks=marks
    @staticmethod    #decorator
    def check():#static method
        print("fuck u")
s1=Student("bibas",89) 
print(s1.name)
print(s1.marks)
print(s1.college_name)#or Student.college_name since it is  a class attribute
s1.check()
