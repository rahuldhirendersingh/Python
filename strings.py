# str represent's string data type. a string is a sequence of character closed within ' ' or " ".

name = "RAM"
print(name)

show = "ramayana"
print(show)

# Slicing in strings

print(show[4])
print(show[-4])
print(show[1:5])
print(show[:5])
print(show[3:])
print(show[:])


print(show[10]) # error: string index out of bound.
print(show[0:20]) # no errors.