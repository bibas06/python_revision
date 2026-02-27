class Car:                            #A->B->C
    @staticmethod                     #base->derived->derived   
    def start():                      #multi-level inheritance               
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")
class Toyotacar(Car):
    def __init__(self,brand):
        self.brand=brand
        print(brand)
class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
c1=Fortuner("diesel")
c2=Toyotacar("mercedes")
c1.start()                       
