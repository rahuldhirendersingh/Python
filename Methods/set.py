s1 = {1,3,5,7,9}
s2 = {2,4,6,8,10,2}
print(s1)
print(s2)

name = "Kartik"
s3 = set(name)
print(s3)

print(min(s1))
print(max(s1))
print(len(s1))
print(sum(s1))
print(3 in s1)

print(s1)
print(s2)

s1.add(13)
print(s1)

# s1.add(15,17) # error

s1.update(s2)
print(s1)

s1.remove(10)
print(s1)

s1.pop()
s1.pop()
print(s1)

s2.clear()
print(s2)

del s2
# print(s2)

print("======================================================")

x = {10,20,30,40}
y = {30,40,50,60}

z = x.union(y)
print(z)

p = x | y
print(p)

z = x.intersection(y)
print(z)

p = x & y
print(p)

z = x.difference(y)
print(z)

z = y.difference(x)
print(z)

z = x - y
print(z)

p = y - x
print(p)

print(x)
print(y)

z = x.symmetric_difference(y)
print(z)

p = y.symmetric_difference(x)
print(p)

z = z ^ y
print(z)

va = (x | y) - (x & y)
print(va)
