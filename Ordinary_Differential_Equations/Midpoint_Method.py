# Chapter05: Ordinary Differential Equations
# Method: Midpoint Method
import math


def midpoint_method(x0, y0, h, x, function):
    # Defining inline function to obtain a value (equation_value) at given x and y
    equation_value = lambda t, w: eval(function)

    # Variable i is showing number of iterations
    i = 1
    print("\n")
    print("i\t\t  Xi\t\t\tYi\t\t")

    # Iterate till x0 is approximated to x for which we need a y-value
    while x0 < x:
        k1 = equation_value(x0, y0)    # f(X(i),Y(i))
        k2 = equation_value(x0 + h/2, y0 + (h/2) * k1)   # f(X(i+h/2),Y(i)+h/2*k1)
        y0 = y0 + (h * k2)
        x0 = x0 + h
        print(i, "\t\t", "%.3f" % x0, "\t\t", "%.4f" % y0)
        i = i+1

    print("\nApproximate solution at x = ", x, " is ", "%.4f" % y0)


def main():
    x0 = float(input("Enter the initial value of X[X0]: "))
    y0 = float(input("Enter the initial value of Y[Y0]: "))
    h = float(input("Enter StepSize [h]: "))
    x = float(input("Enter the value of X at which we need approximation: "))
    function = input("Enter Differential Equation:[t->x and w->y] ")
    midpoint_method(x0, y0, h, x, function)

# Test Case01: X0 =2, Y0= 1, h=1, x=3 and function = 1 +(t-w)**2
# Test Case02: X0 =0, Y0= 1, h=0.25, x=1 and function = math.cos(2*t) + math.sin(3*t)


if __name__== "__main__" :
    main()