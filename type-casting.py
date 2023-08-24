'''

we can convert one type of data to another type, this conversation is called type casting or 
type conversation.

* there are some inbuilt functions for type casting.

- int()
- float()
- complex()
- bool()
- str()

'''

# int
print(int(3.14))
print(int(True))
print(int("555")) # the string should only contain decimal numbers/(base 10) numbers.


# float
print(float(15))
print(float(False))
print(float("90"))


# complex
a = 4
b = 10
print(complex(a, b))
print(complex(5, 20))
print(complex(5, -3))
print(complex(True, False))


# bool
print(bool(" "))
print(bool(""))
print(bool(1))
print(bool(0))


# str -> anything can be converted into strings.
print(str(75))
print(str(3.14))
print(str(12 + 9j))
print(str(True))
