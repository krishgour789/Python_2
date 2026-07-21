# a = {"name":"KrishGour","age":20,"city":"Bhopal"}
# print(a)
# fromkeys creates a new dictionary with the given keys and an optional default value
l = ["krish",23,"Sehore"]
new_dict = dict.fromkeys(["name", "age", "city"], l[0])
print(new_dict)