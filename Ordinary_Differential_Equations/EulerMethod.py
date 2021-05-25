# Chapter05: Ordinary Differential Equations
# Method: Euler Method

import math

def eulerMethod(x0, y0, h, x, function):

    # Defining inline function to obtain a value (equation_value) at given x and y
    equation_value = lambda t, w: eval(function)

    # Variable i is showing number of iterations
    i = 1
    print("\n")
    print("i\t\t  Xi\t\t\tYi\t\t")

    # Iterate till x0 is approximated to x for which we need a y-value
    while x0 < x:
        y0 = y0 + h * equation_value(x0, y0)
        x0 = x0 + h             #Adding step size to update the value of x0
        print(i, "\t\t", "%.3f" % x0, "\t\t", "%.4f" % y0)
        i = i+1

    print("\nApproximate solution at x = ", x, " is ", "%.4f" % y0)


def main():
    x0 = float(input("Enter the initial value of X[X0]: "))
    y0 = float(input("Enter the initial value of Y[Y0]: "))
    h = float(input("Enter StepSize [h]: "))
    x = float(input("Enter the value of X at which we need approximation: "))
    function = input("Enter Differential Equation:[t->x and w->y] ")
    eulerMethod(x0, y0, h, x, function)

# Test Case01: X0 =0, Y0= 0, h=0.5, x=1 and function = t * math.exp(3*t) - 2*w
# Test Case02: X0=0,  Y0=0,  h=0.25, x=1 and function = 3*t +4*w

if __name__== "__main__" :
    main()