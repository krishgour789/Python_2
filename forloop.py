# WAP TO give list of all factors for any number
'''
n = int(input("Enter a Number :"))
factor = []
for i in range(1,n+1):
    if n%i==0:
        factor.append(i)
print("The Factor of ",n," is ",factor)
'''

#  WAP to arrenge all items from list in assending order
# l = [12,45,23,53,56,23,1]
# n = len(l)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

#  WAP to arrenge all items from list in deassending order
# l = [12,45,23,53,56,23,1]
# n = len(l)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if l[j]<l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# l = [23,34,12,33,432,34,777]
# max= l[0]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         max = l[i]
#         l[i],l[i+1]=l[i+1],l[i]
#     else:
#         max = l[i+1]
# print(max)




# l = [23,34,12,33,432,34,777]
# max= l[0]
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         max = l[i]
#         l[i],l[i+1]=l[i+1],l[i]
#     else:
#         max = l[i+1]
# print(max)



# l = [1,0,3,4,0,24,0]
# li = []
# for i in range(len(l)-1):
#     if l[i]!=0:
#         li.append(l[i])
# # n = len(l)-len(li)
# for i in range(len(l)):
#     if l[i]==0:
#         li.append(l[i])
# print(li)

l = [1,1,1,2,3,4,22,3,4,22,33,33]
output = {}
for i in l:
    if i in output:
        output[i]+=1
    else:
        output[i]=1
print(output)