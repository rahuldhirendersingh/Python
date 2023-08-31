t1 = (1,3,5,7,9)
t2 = (2,4,6,8,10)
t3 = t1 + t2
print(t3)
t3 = t1 * 3
print(t3)

print(t3[2])
# t3[3] = 33

print(len(t1))
print(min(t1))
print(max(t1))
print(sum(t1))

print(3 in t1)
print(45 in t1)

print(t3.index(5))

name = "Rizwan"
t4 = list(name)
print(t4)
t4 = tuple(name)
print(t4)

print(t4.count('i'))



student = ('Abhay','Anjali','Bhawna','Disha','Harsh','Rahul')
rollno = tuple(range(1, 7))

Class = zip(student, rollno)
print(Class)

Class = tuple(zip(student, rollno))
print(Class)
