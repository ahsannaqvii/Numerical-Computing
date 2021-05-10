import math

def heun_method(x0, y0, h, x, function):
    equation_value = lambda t, w: eval(function)
    i = 1
    print("\n")
    print("i\t\t  Xi\t\t\tYi\t\t")
    while x0 < x:
        k1 = equation_value(x0, y0)    # f(X(i),Y(i))
        k2 = equation_value(x0 + float(h/3), y0 + (float(h/3) * k1))   # f(X(i+h/2),Y(i)+h/2*k1)
        k3 = equation_value(x0 + float(2*h/3), y0 + (float(2*h/3) * k2))
        y0 = y0 + float(h/4) * (k1 + 3*k3)
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

    heun_method(x0, y0, h, x, function)

# Test Case01: X0 =0, Y0= 1, h=0.25, x=1 and function = math.cos(2*t) + math.sin(3*t)
# Test Case02: X0 =0, Y0= 0, h=0.5, x=1 and function = t * math.exp(3*t) - 2*w

if __name__== "__main__" :
    main()