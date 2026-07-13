# with open('mltxt','ab+') as f:
#     print(f.tell())
#    # f.seek(5)
#     print(f.tell())
#     f.seek(-5,2)
#     print(f.tell())
#     f.seek(2,1)
#     print(f.tell())
#     f.seek(-2,1)
#     print(f.tell())

# with open('m2.txt','r+') as f:
#     print(f.tell())
#     f.read()
#     f.write("hello")
    # f.seek(11,1)
    # print(f.tell())
    # data = f.read(10)
    # print(data)
    # print(f.tell())

with open('m2.txt','a+') as f:
    x = f.read()
    print(x)
    f.seek(0)
    data = f.read()
    print(data)
