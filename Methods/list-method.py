l1 = [2,4,6,8,10]
l2 = [1,3,5,9,11]
l3 = []

print(type(l1))

l3 = l1 + l2
print(l3)

l3 = l1 * 2
print(l3)

l3 = l1 + ['rahul', 'peter']
print(l3)

print(len(l3))
print(l3[3:])
print(min(l1))
print(max(l2))

l3 = ['rahul','ajay','john','shrey','peter']
print(min(l3))
print(max(l3))
print(sum(l1))
print(sum(l2))

print(2 in l1)
print("rahul" in l3)

print("------------------------------------")

a = 'Anjali Singh'
b = list(a)
print(b)

c = list(range(10))
print(c)
c = list(range(20, 70))
print(c)
print(len(c))

l1 = l1 + [25]
print(l1)
l1.append(35)
l1.append(45)
print(l1)
# l1.append(55,65,75) # error: append receives one argument three given

l1.extend([55,65,75])
print(l1)

l2.extend(l3)
print(l2)

l3 = l3 + l1
print(l3)

a = [8,6,2,5,5,25,6,24,62,4,6,2,4]
print(a)
print(a.count(5))

print("-----------------------------------------------------------------")

a = [1,3,5,7,9,11]
b = [2,4,6,8,10]
c = a.extend(b)

print(c)
print(type(c))

print(a.pop())
print(a.pop(2))
a.remove(1)

z = [1,4,6,8,9,1,23,34,1]
z.remove(1)
print(z)

# z.remove(45)
# z.pop(45)

l2 = [5,6,45]
del l2

# print(l2)

print(l1)
print(l1.pop())
print(l1.pop())


name = ['Abhay', 'Anjali', 'Rizwan', 'Satyam', 'Rahul']
print(name.remove("Satyam"))
name.index("Rizwan")
name.insert(3,"Python")
print(name)


print("=============================================================")

l1 = [2,45,67,89,12,32,456,71]
print(l1)

l1.insert(4,100)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)

print(name)
name.sort()
print(name)

print(l1)
l1.sort()
print(l1)
l1.reverse()
print(l1)
