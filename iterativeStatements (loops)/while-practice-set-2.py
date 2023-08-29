
# accept two numbers from the user in the variable m and n, then print all the numbers which are divisible by 5 and the number is also a multiple of 7.

'''
m = eval(input("enter a number: "))
n = eval(input("enter a number: "))

while m <= n:
    if m % 5 == 0 and m % 7 == 0:
        print(m)
    m+=1
'''

# print first 10 odd numbers.

'''
count = 0
num = 1

while True:
    if count == 10:
        break
    if num % 2 != 0:
        print(num)
        count+=1
    num+=1
'''

# print first 10 even numbers.

'''
count = 0
num = 1

while True:
    if count == 10:
        break
    if num % 2 == 0:
        print(num)
        count+=1
    num+=1
'''

# print first m odd numbers where m is imported by the user.

'''
m = eval(input("How many odd number's you want: "))
count = 0
num = 1

while True:
    if count == m:
        break
    if num % 2 != 0:
        print(num)
        count+=1
    num+=1
'''

# count how many even number's are present between m and n.

'''
m = eval(input("enter a number: "))
n = eval(input("enter a number: "))
count = 0

while m <= n:
    if m % 2 == 0:
        count+=1
    m+=1
    
print("There are",count,"even numbers present between m & n")
'''

# print first m odd numbers lies between x and y. where m, x, y are imported by the user.

'''
x = eval(input("enter a number: "))
y = eval(input("enter a number: "))
m = eval(input("how many odd numbers you want? "))

count = 0

while x <= y:
    if count == m:
        break
    if x % 2 != 0:
        print(x)
        count+=1
    x+=1
'''

# print the sum of first 10 even numbers.

'''
num = 1
sum = 0
count = 0

while True:
    if count == 10:
        break
    if num % 2 == 0:
        sum+=num
        count+=1
    num+=1
    
print("The sum of first 10 even number is,",sum)
'''

# print the sum of first n odd numbers.

'''
n = eval(input("how many 'odd numbers sum' do you want? "))
count = 0
sum = 0

num = 1

while True:
    if count == n:
        break
    if num % 2 != 0:
        sum += num
        count+=1
    num += 1

print(sum)
'''

# print the sum of all the even numbers lies between x and y, where x and y are given by the user.

'''
sum = 0

x = eval(input("enter a number: "))
y = eval(input("enter a number: "))

while x <= y:
    if x % 2 == 0:
        sum += x
    x += 1
    
print(sum)
'''


# accept a number from the user and then check wheather the given number is a prime number of not.

num = eval(input("enter a number: "))
start = 2
flag = 0

while start < num:
    if num % start == 0:
        flag = 1
        
    start+=1
    
if flag == 0:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
    
    