class QuardraticEq:
    def __init__(self,a,b,c):
        import math
        d=(b*b)-(4*a*c)
        if(d<0):
            print("Roots are imaginary")
        else:
            x=(-b+math.sqrt(d))/(2*a)
            y=(-b-math.sqrt(d))/(2*a)
            print("x=%.2f"%x,"y=%.2f"%y)
            print("Roots are Real")
            
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
qrdeq=QuardraticEq(a,b,c)

        

