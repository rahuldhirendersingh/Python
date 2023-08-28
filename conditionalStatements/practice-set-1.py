# WAPP which takes two number from the user and then display the greatest number between them.

# number_1 = eval(input("enter the first number: "))
# number_2 = eval(input("enter the second number: "))

# if number_1 > number_2:
#     print(number_1)
    
# else:
#     print(number_2)
    
    
# WAPP which takes three number from the user and then display the greatest number between them.

number_1 = eval(input("enter the first number: "))
number_2 = eval(input("enter the second number: "))
number_3 = eval(input("enter the third number: "))

if number_1 > number_2:
    if number_1 > number_3:
        print(number_1)
    else:
        print(number_3)
elif number_2 > number_3:
    print(number_2)
else:
    print(number_3)
    

# or

print(min(number_1, number_2, number_3), "is the minimum value among the 3 values.")
print(max(number_1, number_2, number_3), "is the maximum value among the 3 values.")

