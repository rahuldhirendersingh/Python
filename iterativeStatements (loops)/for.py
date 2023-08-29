
'''
SYNTAX:

for iterator_var in sequence:
    statements(s)
'''

# print hello 5 times.

for i in range(5):
    print("Hello")
    
# print good morning 50 times.

for i in range(50):
    print("Good Morning")
    
# print first 10 natural numbers.

for i in range(1,11):
    print(i)
    
# print all integers lies bt. 40 % 80

for i in range(40,81):
    print(i)


# print first 20 natural numbers in reverse order.

for i in range(20,0,-1):
    print(i)
    
# print all the odd numbers which are divisible by 17 and lies bt. 400 and 600.

for i in range(400, 600):
    if i % 2 != 0:
        if i % 17 == 0:
            print(i)
    i+=1

# replace 400 and 600 with m & n this time.

m = eval(input("enter a number: "))
n = eval(input("enter a number: "))

for i in range(m, n):
    if i % 2 != 0:
        if i % 17 == 0:
            print(i)
    i+=1
