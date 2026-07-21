# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Krish Gour")
#             sleep(1)
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("Princy Gour")
#             sleep(1)
# t1 = A()
# t2 = B()

# t1.start()
# t2.start()
# t1.join()
# t2.join()


# def reverse(name):
#     a = len(name)
#     reverse = ''
#     for i in range(-1,-a-1,-1):
#         reverse+=name[i]
#     print(reverse)
# a=reverse("Krish")
# a=reverse("Krish gour")

# def count_Fre(name,a):
#         count = 0
#         n = len(name)
#         for i in range(n):
#                 if name[i]==a:
#                     count+=1 
#         print(a,"=",count)

# c=count_Fre("Krrrishr",'r')
# c=count_Fre("pppr",'p')


# WAP to count the number in given string
# def count_num(name):
#         count = 0
#         reverse = ''
#         n = len(name)
#         for i in range(n):
#                 if name[i].isnumeric():
#                     reverse+=name[i]
#         print(name ,"have = ",reverse)
# c=count_num("princy123")

# def remove_duplicate(number):
#     a = list(str(number))
#     l = len(a)
#     for i in range(l-1):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
#     result = int("".join(a))
#     print(result)
# c = remove_duplicate(12321)
# c = remove_duplicate(12321762652)

# def upper(name,r):
#     if r==1:
#         print(name.upper())
#     elif r==2:
#         print(name.lower())
#     elif r==3:
#         print(name.capitalize())
#     elif r==4:
#         print(name.title())
#     else:
#         print("Please choose right way")
# a = upper(input("Enter Your Name :"),int(input("Enter Your Numer :\n 1. For upper\n 2. For Lower\n 3.For Capatalize\n 4. For title\n")))

# class A:
#     def __init__(self):
#         self.a=10
#         self.b=20
#     def display(self):
#         print(self.a)
#         print(self.b)
# obj = A()
# obj.display()


# Class Methods
# class A:
#     x = 2000
#     @classmethod
#     def pull(cls):
#         return cls.x
# obj = A()
# print(A.pull())   # class methods access by using class name
# print(obj.pull()) # class methods acccess by using obj 

# Static Methods
# class A:
#     @staticmethod
#     def pull(x,y):
#         return x+y
# ob = A()
# print(ob.pull(1,2))

#  Method Resolution Order (MRO). 
class A: 
    def m1(self): 
        print("Method m1() is called from class A") 
 
class B: 
    def m1(self): 
        print("Method m2() is called from class B") 
 
class C(B,A): 
    def m3(self): 
        print("Method m3() is called") 
 
obj = C() 
obj.m1() 
obj.m3() 
print(C.mro())
print(C.mro()[0])      # C
print(C.mro()[1])      # A
print(C.mro()[2])      # B

