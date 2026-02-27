class Person:
    __name="bibas"
    def __hello(self):#u cannot access __hello from outside the class
        print("hello fuckers") #u can access it from internal class element
        print(self.__name)                       #i.e.welcome method
    def welcome(self):
        self.__hello()
p1=Person()
p1.welcome()              