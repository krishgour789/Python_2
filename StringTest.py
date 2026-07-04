'''1 . using arithmetic operator in strings   '''
'''a = "Krish"
b = "Gour"
print(a+b)'''
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)

'''a = "Krish"
b = 3
print(a*b)  # Mutiple Operator can perfrom but the condition is one varibale should be integers
'''
'''1 . using comparison operator in strings   '''

# a = "Krish"
# b = "Princy"
# # print(a>b)
# # print(ord('P'))
# # print(ord('K'))
# print(a<b)
# c = "Krish"

# print(ord("a"))
# print(ord("b"))
# print("a">"b")
# print(a==b)

# a = "arish"
# b = "arincy"
# print(a<b)
# print(a==b)

''''1 . using logical operator in strings   '''
# a = "Krish"
# b = "Gour"
# print(a and b)
# print(b and a)
# print(a or b)

# x = "Krish"
# y = ""
# print(x and y)
# print(x or y)


# print("" or "Python" or "Java")

# print(True and False)
# print(False and True)
# print(True and True)
# print(False and False)

# print("Krish" and "Gour")   #Both are truthy, so and returns the last value.

# print(10 or 20)

# CONTROL STATEMENT - 3 types
# conditional statemnt -> if, if-else, if-elif-else
# iterable statement -> for, while
# transfer statement -> continue, break, pass


# if True:
#     a = "Krish"
# print(a)

# while True:
#     a = "Krish"
#     print(a)
#     break
# print(a)


# def test():
#     x = 10
#     print(x)
# test()
# print(x)



# n = 5
# for i in range(1,n+1):
#     print("*"*i,(n-i+1)*"*")

n = 5
i = 0
# while i<=n:
#     print(" "*(n-i),"*"*i)
#     i+=1

# n = 5
# i = 1
# while i<=n:
#     print("*"*(n-i+1)," "*i)
#     i+=1

# while i<=n:
#     print(" "*(n-i),"**"*i)
#     i+=1

# while i<=n:
#     print("*"*i," "*(n-i))
#     i+=1

# while i<=n:
#     print("*"*(n-i+1)," "*i)
#     i+=1

# while i<=n:
#     print(" "*i,"*"*(n-i))
#     i+=1
'''
*****
 ****
  ***
   **
    *'''


# while i<=n:
#     # print(" "*(n-i),"* "*i)
#     print(" "*i,"* "*(n-i))
#     i+=1

# Diamond Star Printing

# n = 5
# i = 0
# while i<=n:
#     print(" "*(n-i)+"* "*i)
#     i+=1
# i = i-2
# while i>0:
#     print(" "*(n-i)+"* "*i)
#     i=i-1


# n=5
# for i in range(0,n+1):
#     print(" "*(n-i),"* "*i)


# n=5
# for i in range(0,n+1):
#     print("* "*(n-i),"* "*i)



# for i in range(n-i,0):
#     print("* "*(n-i)," "*i)



# n = 5
# for i in range(n+1):
#     print("*"*i)

'''
*
**
***
****
*****
'''

# n = 5
# for i in range(n+1):
#     print(" "*(n-i)+"*"*i)
'''  
    *
   **
  ***
 ****
*****
'''


# n = 5
# for i in range(n+1):
#     print(" "*(n-i)+"* "*i)

'''   
    * 
   * * 
  * * * 
 * * * * 
* * * * * '''


# n = 5
# for i in range(0,n):
#     print("*"*(n-i)+" "*i)
'''
*****
**** 
***  
**   
*   '''

# n = 5
# for i in range(0,n):
#     print(" "*i+"*"*(n-i))
'''
*****
 ****
  ***
   **
    *'''

# n = 5
# for i in range(0,n):
#     print(" "*i+"* "*(n-i))
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * '''


# n = 5

# for i in range(0,n):
#     print(" "*(n-i)+"* "*i)
# for i in range(0,n):
#     print(" "*i+"* "*(n-i))
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * '''

# n = 10
# sum = 2
# for i in range(n+1):
#     for j in range(i):
#         print(sum,end=" ")
#         sum+=2
#     print()

# n = 10
# for i in range(n+1):
#     sum = 1
#     for j in range(i):
#         print(sum,end=" ")
#         sum+=2
#     print()
''' 
1 
1 3 
1 3 5 
1 3 5 7 
1 3 5 7 9 
1 3 5 7 9 11 
1 3 5 7 9 11 13 
1 3 5 7 9 11 13 15 
1 3 5 7 9 11 13 15 17 
1 3 5 7 9 11 13 15 17 19 '''


# n = 3
# i = "A"
# while n>0:
#     print(i)
#     i = chr(ord(i)+1)
#     n = n-1



# n = 5
# ch = "A"
# for i in range(n):
#     for j in range(n):
#         print(ch,end=" ")
#         ch = chr(ord(ch)+1)
#     print()  

# n = 5
# ch = "A"
# for i in range(n):
#     ch = "A"
#     for j in range(n):
#         print(ch,end=" ")
#         ch = chr(ord(ch)+1)
#     print()
    

# n = 6
# ch = "A"
# for i in range(n):
#     for j in range(n):
#         print(ch,end=" ")
#         ch = chr(ord(ch)+1)
#     print() 

# print(chr(13934))



# n  = 5
# ch = "A"
# for i in range(n):
#     for j in range(i+1):
#         print(ch,end=" ")
#         ch = chr(ord(ch)+2)
#     print()
'''
A 
C E 
G I K 
M O Q S 
U W Y [ ] '''


n  = 5
for i in range(n):
    ch = "A"
    for j in range(i+1):
        print(ch,end=" ")
        ch = chr(ord(ch)+1)
    print()
'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''