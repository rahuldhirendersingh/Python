d1 = {1:101, 2:102, 3:103, 4:104, 5:105, 12:121}
print(len(d1))
# print(d1[0])
print(d1[3])
print(min(d1))
print(max(d1))
print(sum(d1))
print(1 in d1)
print(101 in d1)

print(d1.keys())
print(d1.values())

d2 = d1
print(d2)
d2.clear()
print(d2)

print(d1)
del d1
# print(d1)

d1 = {1:101, 2:102, 3:103, 4:104, 5:105, 12:121}
d2 = {1:'apple',2:'banana',3:'sinchan',4:'python'}

print(d1, d2)


d1.get(1)
d1.get(10,"NOT FOUND")
print(d1[1])

res = d1.get(3,-1)
print(res)

d3 = {5:"Nobita"}
d2.update(d3)
d2.update({6:'Suzuka'})

print(d2)

d6 = d2.copy()
print(d6)

d2.clear()
print(d2)
print(d6)

print(id(d2), id(d6))

d6[4] = "Giyan"
print(d6)

d6[7] = "Doramon"
print(d6)

del d6[1]
print(d6)

# print(d6.popitem())
# print(d6.popitem())
# print(d6.popitem())
# print(d6)

print("===========================================================================")

for k in d6.keys():
    print(k)
    
for k in d6.keys():
    print(d6[k])
    
for k in d6.values():
    print(k)
    
    
print(d6.items())


for j, k in d6.items():
    print(j, "-->", k)
    
    