
f = open('data.txt', 'r')

# READ

# print(f.read())

# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readline(), end="")

# print(f.readline(4))


# WRITE

f1 = open('abc', 'w') # if the file does'nt exist it'll automatically create the file.
# f1.write('Something ')
# f1.write('People')


# APPEND

f2 = open('abc', 'a')
# f2.write(' Mobile')


# copy everything from data and paste that into abc.

# for i in f:
#     print(i)

for i in f:
    f1.write(i)