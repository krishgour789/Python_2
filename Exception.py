#try - Purpose: Put the code that may cause an error inside try.
# except - Purpose: Put the code that may cause an error inside try.
# a = int(input("Enter a Number : "))
# b = int(input("Enter a Number : "))
# try:
#     c = a/b
#     print("Result =",c)
# except:
#     print("Number Cannot Divide Zero")


# else - Purpose: Runs only if no exception occurs

# x=10
# try:
#     print(x)
# except:
#     print('Please define x first')
# else:
#     print(f"Print {x} Succesfuly")


# finally - Purpose: Runs whether an error occurs or not.

# try:
#     print(x)
# except:
#     print('Please define x first')
# finally:
#     print("Print Succesfuly")




# Raise - Manually create an exception
# age = 16

# if age < 18:
#     raise Exception("You are not eligible to vote.")