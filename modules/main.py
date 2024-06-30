#import calculator and geometry modules from math_operations folder
from math_operations import calculator
from math_operations import geometry

#call add from calculator
result = calculator.add(5, 3)
print("Addition result:", result)

#call subtract from calculator
result = calculator.subtract(10, 4)
print("Subtraction result:", result)

#call rectangle area from geometry
result = geometry.rectangle(6,5)
print("Rectangle area result:", result)

#call circle area from geometry
result = geometry.circle(6)
print("Circle area result:", result)

#call triangle area from geometry
result = geometry.triangle(9,9)
print("Triangle area result:", result)