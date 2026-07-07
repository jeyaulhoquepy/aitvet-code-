class trianglearea:
    def __init__(self, a, b, c):
        import math
        if(a+b)>c and (b+c)>a and (a+c)>b:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("Area of triangle is:", area)
        else:
            print("Invalid triangle sides")
a = float(input("Enter First Arm = "))
b = float(input("Enter Second Arm = "))
c = float(input("Enter Third Arm = "))
triangle = trianglearea(a, b, c)