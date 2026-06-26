# Mathematical Formula Expressions

import math

# 1. Area of Rectangle
length = 10
breadth = 5
area_rectangle = length * breadth
print("Area of Rectangle =", area_rectangle)

# 2. Perimeter of Rectangle
perimeter_rectangle = 2 * (length + breadth)
print("Perimeter of Rectangle =", perimeter_rectangle)

# 3. Area of Circle
radius = 7
area_circle = math.pi * radius * radius
print("Area of Circle =", area_circle)

# 4. Circumference of Circle
circumference = 2 * math.pi * radius
print("Circumference of Circle =", circumference)

# 5. Area of Triangle
base = 12
height = 8
area_triangle = 0.5 * base * height
print("Area of Triangle =", area_triangle)

# 6. Simple Interest
p = 10000
r = 5
t = 2
si = (p * r * t) / 100
print("Simple Interest =", si)

# 7. Compound Interest
amount = p * (1 + r / 100) ** t
ci = amount - p
print("Compound Interest =", ci)

# 8. Average of Three Numbers
a = 20
b = 30
c = 40
average = (a + b + c) / 3
print("Average =", average)

# 9. Swap Two Numbers
x = 10
y = 20
x, y = y, x
print("After Swapping")
print("x =", x)
print("y =", y)

# 10. Celsius to Fahrenheit
celsius = 37
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit =", fahrenheit)

# 11. Fahrenheit to Celsius
f = 98.6
c = (f - 32) * 5 / 9
print("Celsius =", c)

# 12. Square of a Number
num = 6
print("Square =", num ** 2)

# 13. Cube of a Number
print("Cube =", num ** 3)

# 14. Square Root
print("Square Root =", math.sqrt(num))

# 15. BMI Calculation
weight = 60
height = 1.65
bmi = weight / (height ** 2)
print("BMI =", bmi)