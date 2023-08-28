
'''
SYNTAX:

if condition:
    statement 1
    statement 2
    statement 3
    .
    .
    statement n
    
elif condition:
    statement 1
    statement 2
    statement 3
    .
    .
    statement n
    
else:
    statement 1
    statement 2
    statement 3
    .
    .
    statement n
'''

# Q.1

'''
WAPP (write a python program) which accept a number from the user and then check wheather the number is postive, negative or neither positive nor negative. 
'''

number = eval(input("enter a number here? "))

if number > 0:
    print("POSITIVE")
elif number < 0:
    print("NEGATIVE")
else:
    print("NEITHER POSITIVE NOR NEGATIVE")
    
# Q.2
    
''' 
WAPP which accept the age from the user and then check wheather the user is a valid voter or not. 
'''

age = eval(input("enter your age? "))

if age >= 18:
    print("YOU CAN VOTE")
else:
    print("YOU CANNOT VOTE")
    
# Q.3

''' 
WAPP which accepts the marks of 5 different subjects and then display the percentage of the student. '''

maths = eval(input("MATHS SCORE: "))
science = eval(input("SCIENCE SCORE: "))
english = eval(input("ENGLISH SCORE: "))
hindi = eval(input("HINDI SCORE: "))
history = eval(input("HISTORY SCORE: "))

totalMarks = maths + science + english + hindi + history

print("YOU SCORED", (totalMarks / 500) * 100,"%")

