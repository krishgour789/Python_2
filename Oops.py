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


class Car:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    def car2(self,brand):
        print(brand," I love this car")

    def car3(self):
        print(self.color," I like this color")
c1 = Car("Toyoto","Red",7900000)
print(c1.brand,c1.color,c1.price)
    
c1.car2("alto")