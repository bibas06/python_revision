class Student:
    def __init__(self,name,phy,chem,math):
        self.__name=name#has private access now in order to safe private
        self.phy=phy                                        #details
        self.chem=chem
        self.math=math
        avg=(phy+math+chem)/3
        print("hi "+name+" your avg marks is",avg)
s=Student("bibas",89,99,98)
print(s.__name)#it will throw an error

#in order to use private access modifier use __



