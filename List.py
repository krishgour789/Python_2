#list - > list is a mutable data type which is used to store multiple values in a single variable. It is a collection of items which are ordered and changeable. It allows duplicate members.   
# 1> list is heterogeneous data type which means it can store different types of data types in a single list.
# 2> list is also homogeneous data type which means it can store same types of data types in a single list.
# 3> list is mutable data type which means we can change the values of list after it is created.
# 4> list is ordered data type which means the order of the items in the list is preserved.
# 5> list allows duplicate members which means we can store same values in the list multiple times.
# 6> list is a collection of items which are enclosed in square brackets [] and separated by commas.
# 7> Indexing in list starts from 0 and goes upto n-1 where n is the number of items in the list.
# 8> Slicing in list is used to access a range of items in the list. It is done by specifying the start 
#    and end index of the items to be accessed.

# List Methods:
# 1> append() - It is used to add an item to the end of the list. It takes a single argument which is the
#    item to be added.
# 2> extend() - It is used to add multiple items to the end of the list. It takes an iterable as an argument
#    and adds each item from the iterable to the list.
# 3> insert() - It is used to add an item at a specific index in the list. It takes two arguments which are
#    the index at which the item is to be added and the item to be added.
# 4> remove() - It is used to remove the first occurrence of an item from the list. It takes a single argument
#    which is the item to be removed. If the item is not found in the list, it raises a ValueError.
# 5> pop() - It is used to remove an item at a specific index from the list. It takes a single argument which
#    is the index of the item to be removed. If no index is specified, it removes the last item from the list.
# 6> clear() - It is used to remove all items from the list. It does not take any arguments.
# 7> index() - It is used to find the index of the first occurrence of an item in the list. It takes a single
#    argument which is the item to be searched. If the item is not found in the list, it raises a ValueError.
# 8> count() - It is used to count the number of occurrences of an item in the list. It takes a single argument
#    which is the item to be counted. It returns an integer value which is the number of occurrences of the
#    item in the list.
# 9> sort() - It is used to sort the items in the list in ascending order. It does not take any arguments.
#    It modifies the original list and does not return a new list.
# 10> reverse() - It is used to reverse the order of the items in the list.


# a = [1,2,3,4,5,6,7,8,9,10]
# l = [1,2,3]
# a.append(12)       #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
# a.insert(0,1099)   #[1099, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # a.extend(l)        #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
# a.remove(1)          #[2, 3, 4, 5, 6, 7, 8, 9, 10]
# a.pop()                #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.pop(1)                #[1, 3, 4, 5, 6, 7, 8, 9, 10]
# a.reverse()             #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [23,3,4,23,2,3,4]
# a.sort()                #[2, 3, 4, 23, 23]
# print(a.count(23))        #2
# print(a.index(23))        #0
# a.clear()                 #[]
# copy_a = a.copy()           #[23, 3, 4, 23, 2, 3, 4]
# copy_a.append(100)          #[23, 3, 4, 23, 2, 3, 4, 100]
# print(copy_a)               #[23, 3, 4, 23, 2, 3, 4]
                     
# print(a)

# def fun():
#     for i in range(1,11):
#         yield i*i
# # a = fun()
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# for i in fun():
#     print(i)


# def fun():
#     yield 1
#     yield 2
#     yield 3
# a = fun()
# print(a)

# def fun():
#     for i in range(20,30):
#         yield i
# a = fun()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

a = "class"
def fun():
    a = 'Krish Gour'
    def inner():
        a = "Princy"
        print(a)
    inner()
    print(a)
fun()
print(a)

