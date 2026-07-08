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
l = [12,45,23,53,56,23,1]
n = len(l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)