def differential_equation(function):
    return eval(function)


def eulerMethod(x0, y0, h, x, function):
    equation_value = lambda t, w: eval(function)
    #equation_value = differential_equation(function)
    i = 1
    print("\n")
    print("i\t\t  Xi\t\t\tYi\t\t")
    while x0 < x:
        y0 = y0 + h * equation_value(x0, y0)
        x0 = x0 + h
        print(i, "\t\t", "%.3f" % x0, "\t\t", "%.4f" % y0)
        i = i+1

    print("\nApproximate solution at x = ", x, " is ", "%.4f"% y0)


def main():
    x0 = float(input("Enter the initial value of X[X0]: "))
    y0 = float(input("Enter the initial value of Y[Y0]: "))
    h = float(input("Enter StepSize [h]: "))
    x = float(input("Enter the value of X at which we need approximation: "))
    function = input("Enter Differential Equation:[t->x and w->y] ")
    eulerMethod(x0, y0, h, x, function)


if __name__== "__main__" :
    main()