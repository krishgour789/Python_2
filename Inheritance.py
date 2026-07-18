# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname

#     def show(self):
#         print(self.fname,self.lname)
# obj = Person("Jonny","Die")
# obj.show()

# class Student(Person):
    
#     def __init__(self, fname, lname,year):
#         super().__init__(fname,lname)
#         self.graduation = year
#         print("hellooooo")
       
# obj2 = Student("Krish","Gour",2029)
# obj2.show()
# print(obj2.graduation)


# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname

#     def show(self):
#         print(self.fname,self.lname)
# obj = Person("Jonny","Die")
# obj.show()

# class Student(Person):
#     def __init__(self, fname, lname):   #Student object ke andar  "name" naam ka variable dhundo.
#         self.fname=fname
#         self.lname=lname
#         print("hellooooo")
       
# obj2 = Student("Krish","Gour")
# obj2.show()



# class Student:
#     def __init__(self, name):
#         self.name = name

#     def printname(self):
#         print("This is Parent class")
# c = Student("Princy")
# c.printname()

# class CollegeStudent(Student):
#     def __init__(self, name):
#         super().printname()
#         print("Child Constructor")

# p = CollegeStudent("Krish")
# p.printname()




# Polmoryphism Inherintace
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("move !")

# class Car(Vehicle):
#     pass

# class Ship(Vehicle):
#     def move(self):
#         print("Sail !")

# class Plane(Vehicle):
#     def move(self):
#         print("fly !")

# car1 = Car("toyoto",2021)
# Ship1 = Ship("Crise",1999)
# plane1 = Plane("AirIndia",2034)
# for x in (car1,Ship1,plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()
    
# class polymorphism
# class Car:
#     def move(self):
#         print("Drive!")

# class Ship:
#     def move(self):
#         print("Sail!")
# class Plane:
#     def move(self):
#         print("Fly!")
# car1 = Car()
# ship1 = Ship()
# plane1 = Plane()
# for x in (car1,ship1,plane1):
#     x.move()


# class Student:
#     def __init__(self,name,age):
#         self._name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
# obj = Student("krish",34)
# print(obj._name)
# print(obj._Student__age)
# print(obj.get_age())


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    pass
d = Dog()
d.sound()

c = Cat()
c.sound()