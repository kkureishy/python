#square function
def square(side):
    #area formula of square
    area = side*side
    #display area of square
    print("The area of the square is " + str(area) + " square units.")
#circle function
def circle(radius):
    #area formula of circle
    area = radius ** 2 * 3.14
    #display area of circle
    print("The area of the circle is " + str(area) + " square units.")
#call square function with side = 10
square(10)
#call circle function with radius = 10
circle(10)