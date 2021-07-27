"""Looking at Python Files"""
# f = open("files/new.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.seek(14)
# print(f.readline())
#
#
# f.close()
# print(f.closed)
name = input("Enter your name : ")
f = open(name[0]+".txt","w")
f.write(name)
f.close()
# read
# readlines/readline

#     Writing to a file
# f = open("new2.txt","x")
# # write,writelines,writeline
# f.write("Hello")
# f.close()
# f = open("intro.txt","r")
# print(f.read())

# f = open("new.txt","a")
# f.write(" World")
# f.write("\nAppend is just so good")
# f.close()
