
a = 20
b = 30

c = a + b

del a

# print(a)
# print(b)

# STRINGS

a = "My Name is Python"
# print(a)
b = "My name is C++"
# print(b)

name = '''My name is Python
I love Python programming'''

# print(name)

var = '''My name is Rahul
I am a programming student'''

# print(var)


print(a)

print(a[3])
print(a[1:5])
print(a[1:20:3])

print(name)

print(name[5])
print(name[1:7])


# concatenation operator

'''
Between two string you can only use sum operator,
You can only use a multiplication operator which using one string with a number.
'''

print(a + b)
print(a * 2)


a = "My name is Tarzan"
b = "Tar"
c = "Tarzan"

print(b in a)
print(c in a)
print("My" in a)

print(a > b)
print(a > "b")

print("---------------seperation---------------")

b = "My name is India "
c = " My name is India"
d = " My name is India "

print(b.rstrip())
print(c.lstrip())
print(d.strip())


name = "Rahul Rahul"
word = "h"

print(name.find(word))
print(name.find("R"))
print(name.find("a"))

print(name.rfind("a"))
print(name.rfind("u", 7))
print(name.rfind("a", -6))

print(name.find("a", 5))

print("---------------seperation---------------")

a = "Computer is composed of hardware and software both"
b = "m"

print(a.count(b))
print(a.count("z"))
print(a.count("h"))
print(a.count(b, 5))

print(a.index(b))
print(a.index("u"))

print(a.rindex(b))
print(a.rindex("u"))

sen = "i hate python programming language"
d = "love"

s1 = sen.replace("hate", d)
print(s1)

# variable storage variables

a = 1.1
print(type(a))

a = 23
print(id(a))

a = 45
print(id(a))

print("---------------seperation---------------")

print(sen)
l = sen.split()
print(l)
print(type(l))

for x in l:
    print(x)
    
for x in l:
    print(x, end=" ")

print()

name = ["sunny", "bunny", "muny", "money", "honey", "nany"]
s2 = " kumar ".join(name)

print(s2)

s2 = "-".join(name)
print(s2)

print(sen)
l = sen.split("a")
print(l)

print()
print("---------------seperation---------------")


# FEW MORE IMPORTANT METHODS

s = "Python is the mosT easiest prOGgramMing lanGuage"

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

print(s.startswith("Python"))
print(s.startswith("python"))
print(s.startswith("Python is the"))
print(s.startswith("is the"))


print(s)

print(s.endswith("lanGuage"))
print(s.endswith("Ming lanGuage"))
print(s.endswith("graMMing lanGuage"))
print()

print("---------------seperation---------------")

a = "manish"
b = "manish123"
c = "manish@123"
d = "6456985236542"
e = "123a"
f = "PYTHON"
g = "Javascript"
h = "        "
i = "My name is C#"

print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())
print(e.isalnum())

print(a, b, c, d, e, f, g, h, i)

print(a.isdigit())
print(b.isdigit())
print(c.isdigit())
print(d.isdigit())

print(a.islower())
print(b.islower())
print(c.islower())
print(d.islower())
print(f.islower())

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(g.istitle())

print(a.isspace())
print(c.isspace())
print(i.isspace())
print(h.isspace())
