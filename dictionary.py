# a = {"name":"KrishGour","age":20,"city":"Bhopal"}
# print(a)
# fromkeys creates a new dictionary with the given keys and an optional default value
# l = ["krish",23,"Sehore"]
# new_dict = dict.fromkeys(["name", "age", "city"], l[0])
# print(new_dict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   'brands':"Mustang"
# }
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": {"red", "white", "blue"}
# }
# print(thisdict)

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# x = thisdict.get("name")
# print(x)

# x = thisdict.keys()
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

# thisdict = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = thisdict.items()
# print(x)
# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
# car.update({"year":2023})
# print(car)
# car.popitem()
# print(car)
# for x in car:
#     print(x)
# for v in car.values():
#     print(v)

# for x in car:
#     print(car[x])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# mydict1 = thisdict.copy()
# print(id(mydict1))
# print(id(thisdict))


# s = {1,True}
# print(s)
# s = {0,False}
# print(s)
# s = {False,0}
# print(s)

# set3 = {True, False, False}
# print(set3)
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# # tropical = {"pineapple", "mango", "papaya"}
# tropical = "pineapple"
# thisset.update(tropical)
# print(thisset)