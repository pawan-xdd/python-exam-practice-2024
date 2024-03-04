pi = 3.14
diameter = float(input("Enter diameter: "))
print(f"The circle's diamater is {diameter}cm, to find its area, divide {diameter}cm by 2.")
print()
r = diameter/2
print(f"Now, the radius after the dividing {diameter}cm is {r}cm")
print()
area = pi * r * r
print(f"Area of the circle with radius {r}cm is {area}cm^2")
print()