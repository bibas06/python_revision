class Student:
    #default constructor
    def __init__(self):
        pass
    #paramterized constructor
    def __init__(self,fullname,marks_obt):#a constructor which invoke during object creation
        self.name=fullname
        self.marks=marks_obt 
        print(fullname)
s1=Student("bibas",89)#object creation
print(s1.name)
print(s1.marks) 
