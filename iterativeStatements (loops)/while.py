
'''

SYNTAX:

while condition:
    statement..1
    statement..2
    statement..3
    .
    .
    statement..n
    
    increment/decrement statement
    
'''

# print 'hello' 5 times.

i = 0
while i < 5:
    print("Hello")
    i = i + 1

# --------------------------------------
# print "Good Morning" 50 times.

i = 1
while i<=50:
    print("Good Morning", i)
    i+=1

# ---------------------------------------
# print first 10 natural numbers.

i = 1
while i<=10:
    print(i)
    i+=1

# ----------------------------------------
# print the sum of first 20 natural numbers.

i = 1
total = 0
while i<=20:
    total+=i
    i+=1

print("Sum of first 10 natural numbers is: ", total)

# -----------------------------------------

# print all integers lies between 40 to 80.

start = 40
end = 80

while start <= end:
    print(start)
    start +=1

# -----------------------------------------
    
# print first 20 natural numbers in reverse order.

i = 20

while i > 0:
    print(i)
    i-=1
    
