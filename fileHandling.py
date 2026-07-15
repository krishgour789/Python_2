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

# with open('m2.txt','a+') as f:
#     x = f.read()
#     print(x)
#     f.seek(0)
#     data = f.read()
#     print(data)


'r'
# with open('m3.txt','r') as f:
#     x = f.read()     # this is used to read file and if the file doesnt exit it will give an error
#     print(x)
#     f.close()

'w'
# with open('m3.txt','w') as f:
#     x = f.write("I am from sehore")  # if the file exit with same name it will remove all the previose data on file
#     print(x)
#     f.close()


# with open('m4.txt','w') as f:
#     x = f.write("If the file doesn't exit it create a new file and write the content on it")
#     print(x)
#     f.close()


# 3. Append Mode ("a")
# Used to add new data.
# Doesn't delete old data.
# If file doesn't exist
# Creates one.

# with open('m5.txt','a') as f:
#     x = f.write("\nDjango is Also a Good Subject")
#     print(f)
#     f.close()


# 4. Exclusive Mode ("x")
# Creates a new file.
# If file already exists
# Raises an error.

# with open('m6.txt','x') as f:
#     print(f)


# readline()
# Reads only one line.
# with open('m4.txt','r') as f:
#     print(f.readline())       # Read only one line
#     print(f.readline())       # Second call

# with open('m4.txt','r') as f:
#     print(f.readlines())        # Return all data in list form
  

# write()
# Writes one string.
# with open('m4.txt','w') as f:
#     print(f.write("This is best features of itand i love to watch this \n but not only this "))

# writelines()
# Writes multiple strings.
# with open('m7.text','w') as f:
#     print(f.writelines("Django \n Python\n C++\n Java\n"))

# with open('m2.txt','r+') as f:
#     print(f.read())

# Mode	Description
# r+	Read and write. Error if file doesn't exist. Starts at the beginning.
# w+	Read and write. Deletes old data. Creates file if needed.
# a+	Read and write. Appends at the end. Creates file if needed.

# with open('m10.txt','w+') as f:
#     print(f.write("If i will get a chance to work with IT employee then i'll do it"))

# with open('m10.txt','a+') as f:
#     print(f.write("and one day i will also get a letter in my hand"))
#     print(f.tell())
#     print(f.seek(0))
#     print(f.tell())
#     print(f.write("With the helo of seek in start to write at the begining of the fille \n"))
#     print(f.seek(0))
#     print(f.tell())

# with open('m10.txt','r+') as f:
#     print(f.seek(0))
#     print(f.tell())
#     print(f.write("Hii this is from starting \n"))

# with open('m10.txt','r+') as f:
#     print(f.seek(25))
#     print(f.tell())
#     print(f.write(" I am tired"))

# with open('Result39.pdf','rb+') as f:
#     print(f.read())

# import pdfplumber

# with pdfplumber.open("Result39.pdf") as pdf:
#     for page in pdf.pages:
#         text = page.extract_text()
#         print(text)

