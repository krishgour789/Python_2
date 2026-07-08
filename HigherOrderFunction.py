

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


l = eval(input("Enter the list: "))
print(l)
# x = l
# print(x)
# print(x)
# print(type(x))