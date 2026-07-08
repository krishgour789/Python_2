# def function():
#     print("Hello World")
# function()
# function()
# function()
# function()

# def f_to_c(faran):
#     return (faran - 32)*5/9
# # print(f_to_c(70))
# h = f_to_c(80)
# print(h)

# def even_number(n):
#     if n%2==0:
#         return "Ye Even Number Hai :"
#     return "Ye Odd Number Hai"
# print(even_number(4))
# print(even_number(9))


# function with arguments 
# def add(fname,lname):
#     return f"{fname} {lname} is very good"
# print(add("Krish","Gour"))
# print(add("kanha","Gour"))
# print(add("Saloni","Gour"))

# Default Paramter
# def add(lname,fname="krish"):  # we can also pass default values in Parameter
#     return f"{fname} {lname} is very good"
# print(add("Krish","Gour"))
# print(add("kanha","Gour"))
# print(add("Saloni","Gour"))

# print(add())

# def add(fname,lname="Json"):  # we can also pass default values in Parameter
#     return f"{fname} {lname} is very good"
# print(add("sonam","jaiswal"))


# # keyword argument  
# def function(Animal,name):
#     print(f"My {Animal} name is {name}")
#     print(f"{name} is very cute")
# function(name="Choti",Animal="Dog")


# Positional Argument
# def function(Animal,name):
#     print(f"My {Animal} name is {name}")
#     print(f"{name} is very cute")
# function("Dog","Choti")


# Mixing Positional And Keyword Arguments
# def function(fname,lname,age):
#     print(f"my name is {fname} {lname}, and i am {age} years old!!")
# function("krish",age=23,lname="Gour")

# Passing Different Data Types
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

# The data type will be preserved inside the function:
'''
def function(fruits):
    for fruit in fruits:
        print(fruit)
function(["Banana","Kela","Angoor","ketchup"])
function([("Banana","Kela","Angoor","ketchup"),("Mango","Papaya","Pineapple")])
function(("Banana","Kela","Angoor","ketchup"))'''

# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more.

# def function():
#     return ["Banana","Kela","Ketchup"]
# fruit = function()
# print(fruit[0])
# print(fruit[1])
# print(fruit[2])


# def my_function(name,lname,/):
#   print("Hello", name,lname)

# my_function("Krish","Gour")
# my_function(lname="Krish",name="Gour")

# def append_to(element, target=[]):
#     target.append(element)
#     return target

# print(append_to(1)) # Output: [1]
# print(append_to(2)) #
# print(append_to(3)) #


# def dikhao():
#     print("Hello") # Sirf screen par dikhega

# def do_value():
#     return "Hello" # Yeh value aage use karne ke liye milegi

# x = dikhao() # x mein kuch nahi aayega (None)
# y = do_value() # y mein "Hello" aayega
# print(y+"World")

# def dikhao(*args):  # it can take any number of arguments
#     return args

# print(dikhao(1,2,3,4,5,"Krish","Gour"))  # Output: (1, 2, 3, 4, 5, 'Krish', 'Gour')

# def dilhoa(**kwargs): # it can take any number of keyword arguments
#     return kwargs

# print(dilhoa(name="Krish", lname="Gour"))  # Output: {'name': 'Krish', 'lname': 'Gour'}


# def fun(a=int(input("enter a number")),b=int(input("enter a  number"))):
#     return a+b
# print(fun())


# print(print("hello"))

# def function():
#     print("Hello World")
# function()
# res = function()
# print(res)

# def display():
#     a = 10
#     b = 20

# display()
# res=display()
# print(res)




# Positinal Arguments
# def function(a,b):
#     return a+b
# print(function(3,4))

# Default Arguments
# def sum(b,a=20):
#     return a+b
# print(sum(10,90))

# def sum(a=20,b):  # It will give an error bcz parameter without a default follows parameter with a default
#     return a+b
# print(sum(10,90))

# Keyword Argumrnts
# def sum(a,b):
#     return a*b
# print(sum(b=10,a=90))

# Variable length Arguments
# def sum(*n):
#     total = 0
#     for i in n:
#         total+=i
#     print("The total sum is :",total)
# sum(10,20,30,50)


# key word variable length arguments
# def display(**kwargs):
#     for i,v in kwargs.items():
#         print(f"{i}:{v}")
# display(name="KrishGour",age=23)

# def sum():
#     global a
#     a = 10
#     print(a)
# def m2():
#     print(a)
# sum()
# m2()

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s+=i*i
# print(s)

# def student(name,age=19,*n,**kwargs):
#     print(name)
#     print(age)
#     print(n)
#     for i,v in kwargs.items():
#         print(f"{i}:{v}")
    
# student("KrishGour",20,("Python","Djnago","MySql"),Class10="MNA")


def stu(name,age=19,*n,school,city="Bhopal",**x):
    print(name)    #Positional Arguments
    print(age)    #Deafult Positional Arguments
    print(n)   #Variable length Positional Arguments (*n)
    print(school)     #key-word  Arguments
    print(city)    #default keyword argument
    print(x)      #Variable length key-word Arguments (*n)

stu("KrishGour",20,10,30,42,school="MNA",city="Sehore",x=10,y=10)



# examples of function 
# def add(a,b):
#     return a+b
# print(add(5,3))

# def xyz(*n):
#     print(n)
# xyz()

# def xyz(**n):
#     print(n)
# xyz()

# def xyz(b,a=10):
#     print(a,b)
# xyz(20)

# print(list())



# function Variable are  mainly three types

# global 
# local 
# non local = used in nested fucntion