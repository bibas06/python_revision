class Car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False
    def  start(self):#hiding the unnecessary details without any internal 
        self.acc=True                                     #implementation
        self.clutch=True
        print("car started...")
car1=Car()#it focuses on necessary details
car1.start()      
