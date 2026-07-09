

# MAP FUNCTION (HIGH ORDER FUNCTION)
# l1 =[20,12,32,120]
# l2 =[60,42,352,150]
# l3 =[60,42,352]
# def sum(x,y,z):
#     return x+y+z
# res = map(sum,l1,l2,l3)
# print(res)
# print(list(res))



# Filter -> It will return collection order
# a = [1,2,3,4,6,7]
# def even(x):
#     if x%2==0:
#         return x
# res = filter(even,a)
# print(res)
# print(list(res))


# Reduce 

# import functools


# a = [1,2,3,4,6,7]
# def even(x):
#     return sum(x)
# res = functools.reduce(even,a)
# print(res)



# # Decorator 
# def chai():
#     print("Gas On")
#     print("Chai Ban Gayi")
#     print("Gas Off")
# chai()

# def Kitchen(func):
#     def inner(name):
#         print("Gas On kr do")
#         func(name)
#         print("Gass of kr do")
#     return inner
# # @Kitchen
# # def Chai():
# #     print("chai bn gyi hai")
# # Chai()
# @Kitchen
# def Item(name):
#     print(f"{name} bn gyi hai" )
# Item("Maggie")
# Item("Tea")


# def greet(func):
#     def inner(name):
#         print("hello")
#         func(name)
#         print("ThankYou")
#     return inner
# @greet
# def person(name):
#     print(f"Welcome {name}")
# person("krish Gour")


# a = "Krish"
# b = "Krish"
# print(id(a))
# print(id(b))

# a = 12
# b = 12
# print(id(a))
# print(id(b))

# a = [1,2,3]
# b = [1,2,3]
# print(id(a))
# print(id(b))
# a[1]=3
# print(a)


# l = [1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     if x%2==0:
#         return x
# res = filter(even,l)
# print(list(res))


# l = [1,2,3,4,5,6,7,8,9,10]
# def odd(x):
#     if x%2!=0:
#         return x
# res = filter(odd,l)
# print(list(res))

# l = [1,2,3,4,5,6,7,8,9,10]
# def less_than_5(x):
#     if x<5:
#         return x
# res = filter(less_than_5,l)
# print(list(res))


from functools import reduce
# l = [23,12,32,34,12,43]

# def max_no(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# res = reduce(max_no,l)
# print(res)

# def sum(x,y):
#     return x+y
# res = reduce(sum,l)
# print(res)
        
        
# l = eval(input("Enter the list: "))
# def max_no(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# res = reduce(max_no,l)
# print(res)


# l = eval(input("Enter the list: "))
# print(l)
# # x = l
# # print(x)
# # print(x)
# # print(type(x))

# a = [1,2,3,2,3,"p","l","m"]
# print(a.index(2))
# print(a.index("p",3,7))
# print(a.index("l",3,7))
# print(a.index("m",3))

# def changecase(func):
#     def inner(*n,**m):
#         print("welcome")
#         return func(*n,**m).upper()
#     return inner
# @changecase
# def greet(name):
#     return f"Hello {name}"  
# print(greet("Krish Gour"))
# print(greet("Princy"))


# def changecase(n):
#     def changecase(func):
#         def inner(name):
#             if n==1:
#                 return func(name).upper()
#             else:
#                 return func(name).lower()
#         return inner
#     return changecase
# @changecase(1)
# def greet(name):
#     return f"My name is {name}"
# print(greet("krish gour"))



# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)
# print(myfunction())


# def number(n):
#     return lambda x:x*n
# double = number(3)
# double1 = number(6)
# print(double(4))
# print(double1(4))


def outer_fun(main_func):
    def inner(x,y):
        print("hello")
        # return x*y
        main_func(x,y)
        print("After execution")
    return inner
# @outer_fun
def main_func(x,y):
    print(x+y)
res = outer_fun(main_func)    # We can also use decorator @outer_fun instead of this line
res(10,20)                    
# main_func(10,20)    

# @outer_fun
# def xyz(x,y):
#     print(x//y)
# xyz(20,2)


# if True:
#     a = 10
# print(a)
