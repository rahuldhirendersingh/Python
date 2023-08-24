# Identity Operators -> Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


x = 'rony'
y = 'rony'

# is
print(x is y) # returns true if both value's are same.

# is not
print(x is not y) # return false if both value's are different.
