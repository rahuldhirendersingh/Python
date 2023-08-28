'''
WAPP which takes diameter of a circle and then print the area and circumference of the circle.
'''


# diameterCircle = eval(input("enter the diameter of circle: "))
# radiusCircle = diameterCircle / 2

# areaOfCircle = (22 / 7) * radiusCircle ** 2
# print(areaOfCircle)

# circumferenceOfCircle = 2 * (22 / 7) * radiusCircle
# print(circumferenceOfCircle)

'''
WAPP which takes base and height of a triangle and then print it's area.
'''


# baseTriangle = eval(input("enter base of triangle: "))
# heightTriangle = eval(input("enter height of triangle: "))

# areaOfTriangle = 1 / 2 * baseTriangle * heightTriangle
# print(areaOfTriangle)

'''
WAPP which takes length and breath of a rectangle and then check wheather it is a square or not.
'''


# lengthRectangle = eval(input("enter the of the rectangle: "))
# breathRectangle = eval(input("enter the breath of the rectangle: "))

# if lengthRectangle == breathRectangle:
#     print("the rectangle is indeed a sqaure.")
# else:
#     print("the rectangle is not an sqaure.")
    
'''
WAPP which takes marks of 4 subject from the student and then display the result grade as per the following criteria.

90> - A
80> - B
70> - C
60> - D
50> - P
50< - F
'''

maths = eval(input("enter your marks for maths: "))
econ = eval(input("enter your marks for economics: "))
english = eval(input("enter your marks for english: "))
geography = eval(input("enter your marks for geography: "))

totalMarks = maths + econ + english + geography
percentage = (totalMarks / 400) * 100
print(percentage)

if percentage > 100:
    print("Invalid Input's Given")
elif percentage >= 90:
    print('A')
elif percentage >= 80:
    print('B')
elif percentage >= 70:
    print('C')
elif percentage >= 60:
    print('D')
elif percentage >= 50:
    print('P')
else:
    print('F')