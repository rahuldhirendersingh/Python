
# print the table of n.

'''
n = int(input("enter a number: "))
count = 1

print("Here is the table of", n)
while count <= 10:
    print(n * count)
    count+=1
'''

# print all the multiple of 7 lies between m & n.

'''
m = eval(input("enter the starting value: "))
n = eval(input("enter the ending value: "))

while m <= n:
    if m % 7 == 0:
        print(m)
    m+=1
'''

# print all the even numbers lies between 120 & 240.

'''
a = 120
while a <= 240:
    if a % 2 == 0:
        print(a)
    a+=1
'''
 
# print all the odd numbers lies between 400 & 500.

'''
a = 400
while a <= 500:
    if a % 2 != 0:
        print(a)
    a+=1
'''


# print all the even number's between m and n, m & n are given by user.

'''
m = eval(input("enter the initial number: "))
n = eval(input("enter the last number: "))

print("Here are all the even numbers between",m,"and",n)
while m <= n:
    if m % 2 == 0:
        print(m)
    m+=1
'''

# print all the odd number's between m and n, m & n are given by user.

'''
m = eval(input("enter the initial number: "))
n = eval(input("enter the last number: "))

print("Here are all the odd numbers between",m,"and",n)
while m <= n:
    if m % 2 != 0:
        print(m)
    m+=1
'''
    
# print all the odd numbers that are divisible by 17 lies between 400 & 600.

a = 400
b = 600

while a <= b:
    if a % 2 != 0:
        if a % 17 == 0:
            print(a)
    a+=1
    
# same question as above just replace 400 & 600 with m and n imported by the user.

a = eval(input("enter the first number: "))
b = eval(input("enter the last number: "))

while a <= b:
    if a % 2 != 0:
        if a % 17 == 0:
            print(a)
    a+=1
    
    