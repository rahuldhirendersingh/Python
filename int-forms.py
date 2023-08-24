'''
We can use int data type to represent whole numbers (integral values).
We can represent int values in following ways,

1.) Decimal form -> default number system in python. allowed digits (0-9)
2.) Binary form
3.) Octal form
4.) Hexa decimal form
'''

# binary form (allowed value:- 0, 1) -> prefixed with 0b 

a = 10
print(bin(a))
print(0b1010)

# octal form (allowed value:- 0 to 7) -> prefixed with 0o
b = 50
print(oct(b))
print(0o62)

# hexa-decimal form (allowed value: 0 to 9 then a-f) -> prefixed with 0x
c = 100
print(hex(c))
print(0x64)