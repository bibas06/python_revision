class Student:
    def welcome(self,name):
        self.name=name#this is called encapsulation i.e.wrapping
        print(self.name)       #data and functions into a single unit
s1=Student()
s1.welcome("bibas")
print(s1.name)    
