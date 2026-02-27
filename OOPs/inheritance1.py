class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")
class Toyotacar(Car):#single inheritance
    def __init__(self,name):#no need of specifying function name (__init__)
        self.name=name
        print(name)      #dislike other function(vehicle) 
car1=Toyotacar("fortuner")         #car1.vehicle("<name>")
car2=Toyotacar("mahindra")
print(car1.start())      