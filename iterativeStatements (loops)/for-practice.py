
# print all the number that are divisible by 5 and 7, lies between m and n.

m = eval(input("enter a number: "))
n = eval(input("enter a number: "))

for i in range(m, n):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


# print the table of n.

n = int(input("enter a number: "))

for i in range(1, 11):
    print(n * i)


# print all the multiple of 7 lies between m & n.

m = eval(input("enter a number: "))
n = eval(input("enter a number: "))

for i in range(m, n):
    if i % 7 == 0:
        print(i)

 
# print all the odd numbers lies between m and n.

m = eval(input("enter a number: "))
n = eval(input("enter a number: "))

for i in range(m, n):
    if i % 2 != 0:
        print(i)

    
# print first 10 odd numbers.

for i in range(1,20+1):
    if i % 2 != 0:
        print(i)
       
# print first n even numbers.

n = eval(input("enter a number: "))

for i in range(1,n*2+1):
    if i % 2 == 0:
        print(i)

# print the sum of first n even numbers.

sum = 0
n = eval(input("enter a number: "))

for i in range(1,n*2+1):
    if i % 2 == 0:
        sum+=i
        
print(sum)
        

