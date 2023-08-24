# data type represent the type of data present inside a variable.

a = 10
print(type(a)) # int

b = 10.14
print(type(b)) # float

c = "rahul"
print(type(c)) # str

d = 5 + 12j
print(type(d)) # complex

e = True
print(type(e)) # bool

'''
In python we are not required to specify the type explicitly. based on the value provided,
the type will be assigned automatically. Hence python is a dynamically typed language.
'''

x = [5, 'rahul', True, 3.14] # list
print(type(x))

y = (88, 95.25, 'sanjay') # tuple
print(type(y))

z = {41, 'john', 88.8} # set
print(type(z))



# dict

phones = {'rahul':'iPhone 13', 'john':'motorola g52', 'radha':'iPhone 11'} 
print(phones['rahul'])
print(type(phones))



# range

p = range(10) # form 1
print(type(p))
print(list(p))
print(p[4])


q = range(10, 20)
print(type(q))
print(list(q))
print(q[4])


r = range(30, 60, 3)
print(type(r))
print(list(r))
print(r[4])

# ---FILE END'S HERE---