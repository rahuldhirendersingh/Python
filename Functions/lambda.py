# Python Lambda

'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax,
lambda arguments : expression
The expression is executed and the result is returned:
'''

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b

print("Multiply two number.")
a = eval(input("enter a number: "))
b = eval(input("enter a number: "))

print(x(a, b))



x = lambda a, b, c : a + b + c

print("Add three numbers.")
a = eval(input("enter a number: "))
b = eval(input("enter a number: "))
c = eval(input("enter a number: "))

print(x(a, b, c))
