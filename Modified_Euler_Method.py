#More accurate than Euler method
import math


def modified_euler(x0, y0, h, x, function):
    equation_value = lambda t, w: eval(function)
    i = 1
    print("\n")
    print("i\t\t  Xi\t\t\tYi\t\t")
    while x0 < x:
        k1 = h * equation_value(x0, y0)    # hf(X(i),Y(i))
        k2 = h * equation_value(x0 + h, y0 + k1)   # hf(X(i+1),Y(i)+k1)
        y0 = y0 + 1/2 * (k1 + k2)
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
    modified_euler(x0, y0, h, x, function)

# Test Case01: X0 =2, Y0= 1, h=1, x=3 and function = 1 +(t-w)**2
# Test Case02: X0 =0, Y0= 1, h=0.25, x=1 and function = math.cos(2*t) + math.sin(3*t)

if __name__== "__main__" :
    main()