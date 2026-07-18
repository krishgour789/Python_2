# class Student:
#     name = "KrishGour"
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)

# class Car:
#     def __init__(self):
#         print("toyoto")
#         print(id(self))
# c1 = Car()
# print(id(c1))


# class Car:
#     def __init__(self,brand,color,price):
#         self.brand = brand
#         self.color = color
#         self.price = price
        
#     def car2(self,brand):
#         print(brand," I love this car")

#     def car3(self):
#         print(self.color," I like this color")
# c1 = Car("Toyoto","Red",7900000)
# print(c1.brand,c1.color,c1.price)
    
# c1.car2("alto")




# class Student:
#     "Hello Everyone"    # It is Document for class to princt this line we use     print(obj.__doc__)
#     def fun(self):
#         "I am Python Full stack Developer"   # if this document written in function   print(obj.fun.__doc__)
#         print("Krish Gour")
# obj = Student()
# obj.fun()
# print(obj.__doc__)
# print(obj.fun.__doc__)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"I am {name} and I am {age} years old")

#     def vil(self,name,age):
#         print(f"{self.name} is always with me")
#         print(f"{age} years old")

# # obj = Student("krish",23)
# # obj.fun()
# obj2 =Student("KrishGour",23)
# obj2.vil("sapna",34)
# # obj.vil()


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"Hello, my name is {self.name}")


# # Create an object
# p1  = Person("John",36)
# p1.greet()
# # Call the greet method

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(self.name + " Says Woof!")
# d1 = Dog("Buddy",3)
# d1.bark()


# Inside the editor, complete the following steps:
# Create a class called Car
# Add an __init__ method with a brand parameter, and store it as a property
# Add a method called show that prints the brand
# Create an object c1 of the Car class with brand "Ford"
# Call the show method on c1

# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#     def show(self):
#         print(self.brand)
# c1 = Car("Ford")
# c1.show()


# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
    
# obj = Car("Toyoto","Black")
# print(obj.brand)
# print(obj.color)


# obj.color="White"

# print(obj.color)


# class MNA:
#     principle = "Deepak"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# obj = MNA("Krish",20)
# print(obj.principle)
        

# class Student:
#     school = "ABC School"

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Krish")
# s2 = Student("Rahul")

# s1.school = "XYZ School"

# print(s1.school)
# print(s2.school)
# print(Student.school)


# class Student:
#     school = 'JNV'
#     def __init__(self,name):
#         self.name = name 
#     def display(self):
#         message = "Welcome"
#         print(message)
#         print(self.name)
# s1 = Student("Himashi")
# print(s1)
# s1.display()
# print(Student.school)

# class Student:
#     def __init__(self,name):
#         self.name = name
#         print(self.name)
# s1 = Student("Himashi")

# class Student:
#     school = "JNV"
#     def __init__(self,name):
#         Student.name = name
#     def display(self):
#         Student.graduation="Btech"
        
# s1 = Student("himanshi")
# print(s1.name)
# print(s1.school)
# s1.display()
# print(s1.graduation)




# class Tu:
#     @staticmethod
#     def greet():
#         print("WELCOME")
# Tu.greet()


# class Student:
#     school="JNN"
#     @classmethod
#     def show_class(cls):
#         print("school",Student.school)
# s1=Student()
# s1.show_class()
# print("After change")
# Student.school="RKDF"
# s2= Student()
# s2.show_class()

# class Calculator:
#     print("This is my Calculator")
#     @staticmethod
#     def calc(n):
#         for i in range(1,n+1):
#             print(i*i)
# c1 = Calculator()
# c1.calc(int(input("Enter a Number : ")))

# for i in range(1,10):
#     print(i**2)
#     print(i*i)


# Encapsulation
# class a:
#     __x = 10
#     def show(self):
#         print("hello")
# class b(a):
#     pass
# obj = b()
# print(obj._a__x)
# print(dir(a))


# class Bank:

#     def __init__(self):
#         self.__balance = 10000

#     def check_balance(self):
#         print(self.__balance)
# b = Bank()
# b.check_balance()
# b.__balance()


# class Bank:
#     def __init__(self):
#         self.balance = 10000

# b = Bank()
# print(b.balance)
# b.__balance = 5000000
# print(b.__balance)


class Bank:
    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

b = Bank()

b.deposit(500)
b.show_balance()
b.__balance = 5000000
b.show_balance()
print(b.__balance)
print(b.__dict__)