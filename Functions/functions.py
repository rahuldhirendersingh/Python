# functions are used to divide the code into smaller more maintainable and potencially more reusable chunks.

def greet():
    print("Hi there")
    print("Welcome aboard")
    
    
greet()

# -> Parameters & Arguments

def greet(first_name, last_name): # parameters
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
    
    
greet("John", "Smith") # arguments
# greet("Peter") # you need to specify arguments for each parameter.
# print(greet("rahul", "singh")) # after printing the essential output it'll print none. because all function by default return None, until you return something specificly.


# In programming we have two types of functions

'''
1.) Perform a task
2.) Return a value
'''

# Usign return

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Peter")
print(message)
# OR
print(get_greeting("Mosh"))

 
 
#  keyword argument

def increment(number, by):
    return number + by


print(increment(2, 7))
print(increment(2, by=9))



# default arguments

def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, 5))



# *args and **args

def multiply(*numbers):
    # print(numbers)
    
    total = 1
    for number in numbers:
        # print(number)
        total *= number
    return total
    

answer = multiply(2,3,4,5,6)
print(answer)



def save_user(**user):
    # print(user)
    print(user["name"])    
    
    
save_user(id = 1, name = "thor", age = 1500, planet="asgard")


# SCOPE

def greet(name):
    mes = "a" # any variable defined inside this block stays here. LOCAL VARIABLE
        
    
# print(mes) # error
# print(name) # error


def mes():
    num = 45


# print(num) # error

# local variable are temperarly stored, as after you run the function there is no use of it.


# PASS

def nothing():
    pass


