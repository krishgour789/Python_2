# l = []
# for i in range(1,6):
#     l.append(i*i)
# print(l)

# x = [i*i for i in range(1,6)]
# print(x)

# x = [i for i in range(1,6) if i%2==0]
# print(x)

# numbers = [1,2,3,4,5,6,7,8]
# even = [i for i in numbers if i%2==0]
# print(even)



# x = [x for x in range(1,11)]
# print(x)

# x = "Krish"
# y =[i.upper() for i in x]
# print(y)

# dict = {i:i*i for i in range(10)}
# print(dict)


# sqaure = []
# for i in range(5):
#     sqaure.append(i**2)
# print(sqaure)

# x = [i**2 for i in range(10)]
# print(x)

# even = []
# for i in range(5):
#     if i%2==0:
#         pass     
# print(even)

# x = [i%2==0 for  i in range(5)]
# print(x)

# x = [i for i in range(5) if i%2==0]
# print(x)

# even = [x for x in range(1,6) if x%2==0]
# print(even)

# x = ["Even" if i%2==0 else "Odd" for i in range(1,6)]
# print(x)

# l = [1,2,3,4,5]
# data = [l[i] if l[i]!=6 else l.append(6) for i in range(7)]
# print(data)

# mydict = {'maths':30,'science':50,'history':80}
# myres = {subject:marks+5 for subject,marks in mydict.items()}
# print(myres)


# mydict = {'maths':30,'science':50,'history':80}
# myres = {subject:marks+5 for subject,marks in mydict.items() if marks>50}
# print(myres)

# mydict = {'maths':30,'science':50,'history':80}
# myres = {subject:"PAss" if marks>45 else "Fail" for subject,marks in mydict.items()}
# print(myres)

# {'maths': 'Fail', 'science': 'PAss', 'history': 'PAss'}

# mydict = {'maths':30,'science':50,'history':80}
# myres = {subject:"PAss" if marks>45 else "Fail" for subject,marks in mydict.items()}
# print(myres)

# l = [x for x in range(10) if x%3==0]
# print(l)
# l = [1,2,3,4,5]
# n = len(l)

# l = [l1.append(l[i]) if i<n else l1.append(int(input("Enter new number :"))) for i in range(n+1)]

even_dict = {i:i if i%2==0 else i for i in range(11)}
print(even_dict)