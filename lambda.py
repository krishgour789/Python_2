# res = lambda x,y:x+y
# print(res(3,4  ))
# res = lambda x,y:print(x+y)
# res(3,4  )
# res = lambda x,y:x+y
# x=res(3,4)
# print(x)
# res = lambda x,y:print(x+y)
# print(res)

# res = lambda x,y:print(x+y)
# x=res(3,4 )
# print(x)
# print(type(x))

# a = [1,2,3,4,5]
# y = list(map(lambda x:x*x,a))
# print(y)


# res = lambda x,y:print(4)
# print(res(3,4))
# res = lambda x,y:print(x+y)
# res(3,4 )



# res = lambda x,y:x+y
# res(3,4)

# l1 = [1,2,3,4]
# l2 = [3,4,5,6]
# res = map(lambda x,y:x+y,l1,l2)
# print(list(res))

# l1 = [1,2,3,4]
# res = filter(lambda x:x%2==0,l1)
# print(list(res))

# l1 = [1,2,3,4]
# res = filter(lambda x:x%2!=0,l1)
# print(list(res))

from functools import reduce
l1 = [1,2,3,4]
res = reduce(lambda x,y:x if x<y else y,l1)
print(res)
