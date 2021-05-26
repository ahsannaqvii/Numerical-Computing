import math
from tabulate import tabulate
import sympy as sp
import os


# -------------------------------------------------------

array = []
n =-1

# -------------------------------------------------------
def bisection_method(a, b,f,error,truevalue,roundvalue):  #bisection method
    global n
    global array
    str1="."+str(roundvalue)+"f"
    n+=1
    c = (a + b) / 2
    if truevalue:
        array.append([n, a, b, c, f(c), round(abs(truevalue-c),roundvalue)])
    else:
        array.append([n,a,b,c,f(c),round(abs(c-array[n-1][3]),roundvalue) if n>0 else "-"])

    if truevalue==0 and ((round(abs(c-array[n-1][3]),roundvalue) < error and n>0) or abs(f(c))==0):

        print(tabulate(array,headers=["Iteration","a","b","c","f(c)","Estimated Absolute Error"],floatfmt=str1))
        print("\n\nReal Root: ",round(c,roundvalue))
        n=-1
        array.clear()

    elif truevalue and ((round(abs(c-truevalue),roundvalue) and n>0) or abs(f(c))==0):
        print(tabulate(array, headers=["Iteration", "a", "b", "c", "f(c)", "Absolute Error"], floatfmt=str1))
        print("\n\nReal Root: ", round(c, roundvalue))
        n = -1
        array.clear()

    else:
        if (f(a) < 0):
            anegative = True
        else:
            anegative = False
        if anegative:
            if f(c) > 0:
                b = c
            elif f(c) < 0:
                a = c
        else:
            if f(c) > 0:
                a = c
            elif f(c) < 0:
                b = c

        bisection_method(a, b,f,error,truevalue,roundvalue)

# -------------------------------------------------------

def regula_falsi_method(a, b,f,error,truevalue,roundvalue):   #regula falsi method
    global n
    global array
    str1 = "." + str(roundvalue) + "f"
    n+=1
    c = (a*f(b)-b*f(a))/(f(b)-f(a))
    if truevalue:
        array.append([n, a, b, c, f(c), round(abs(truevalue - c),roundvalue)])
    else:
        array.append([n, a, b, c, f(c), round(abs(c - array[n - 1][3]),roundvalue) if n > 0 else "-"])

    if truevalue==0 and ((round(abs(c-array[n-1][3]),roundvalue) < error and n>0) or abs(f(c))==0):

        print(tabulate(array, headers=["Iteration", "a", "b", "c", "f(c)", "Estimated Absolute Error"], floatfmt=str1))
        print("\n\nReal Root: ", round(c, roundvalue))
        n = -1
        array.clear()

    elif truevalue and ((round(abs(c - truevalue), roundvalue) and n > 0) or abs(f(c)) == 0):
        print(tabulate(array, headers=["Iteration", "a", "b", "c", "f(c)", "Absolute Error"], floatfmt=str1))
        print("\n\nReal Root: ", round(c, roundvalue))
        n = -1
        array.clear()

    else:
        if (f(a) < 0):
            anegative = True
        else:
            anegative = False
        if anegative:
            if f(c) > 0:
                b = c
            elif f(c) < 0:
                a = c
        else:
            if f(c) > 0:
                a = c
            elif f(c) < 0:
                b = c

        regula_falsi_method(a, b,f,error,truevalue,roundvalue)

# -------------------------------------------------------

def newton_method(P0,f,f_prime,error,truevalue,roundvalue):   #newton method
    global n
    global array
    str1 = "." + str(roundvalue) + "f"
    n+=1
    P=P0
    if truevalue:
        array.append([n, P, f(P),round(abs(P - truevalue),roundvalue)])
    else:
        array.append([n, P, f(P),round(abs(P - array[n - 1][1]),roundvalue) if n > 0 else "-"])
    P=P0-(f(P0)/f_prime(P0))
    if truevalue==0 and ((round(abs(P-array[n-1][1]),roundvalue) < error and n > 0) or abs(f(P))==0):
        print(tabulate(array, headers=["n", "P","f(P)", "Estimated Absolute Error"],floatfmt=str1))
        print("\n\nReal Root: ", round(P,roundvalue))
        n = -1
        array.clear()

    elif truevalue and ((round(abs(P - truevalue),roundvalue) < error and n > 0) or abs(f(P))==0):
        print(tabulate(array, headers=["n", "P","f(P)", "Absolute Error"], floatfmt=str1))
        print("\n\nReal Root: ", round(P,roundvalue))
        n = -1
        array.clear()

    else:
        newton_method(P,f,f_prime,error,truevalue,roundvalue)

# -------------------------------------------------------

def secant_method(P0, P1,f,error,truevalue,roundvalue):   #secant method
    global n
    global array
    str1 = "." + str(roundvalue) + "f"
    n+=1
    P = (P0*f(P1)-P1*f(P0))/(f(P1)-f(P0))
    if truevalue:
        array.append([n, P0, P1, P,f(P), round(abs(truevalue - P),roundvalue)])
    else:
        array.append([n, P0, P1, P,f(P), round(abs(P - array[n - 1][3]),roundvalue) if n > 0 else "-"])

    if truevalue == 0 and ((round(abs(P - array[n - 1][3]),roundvalue) < error and n > 0)or abs(f(P))==0):

        print(tabulate(array, headers=["Iteration", "P0", "P1", "P","f(P)", "Estimated Absolute Error"], floatfmt=str1))
        print("\n\nReal Root: ", round(P, roundvalue))
        n = -1
        array.clear()

    elif truevalue and ((round(abs(P - truevalue),roundvalue) < error and n > 0) or abs(f(P))==0):
        print(tabulate(array, headers=["Iteration",  "P0", "P1", "P","f(P)", "Absolute Error"], floatfmt=str1))
        print("\n\nReal Root: ", round(P, roundvalue))
        n = -1
        array.clear()

    else:

        secant_method(P1, P,f,error,truevalue,roundvalue)


# --------------------------------------------------------
#main:
print("Installing required modules")
os.system("pip install tabulate sympy mpmath")


choice="y"

while(choice=="y" or choice =="Y"):
    os.system("cls")
    str_expression=input("Enter equation: ")
    error=float(input("Enter tolerance error value: "))
    roundvalue=int(-1*math.log10(error))+1
    truevalue=float(input("Enter true value of root if known, otherwise enter 0: "))
    print()
    x,y=sp.symbols('x y')
    f=sp.lambdify(x,sp.sympify(str_expression))

    ch=int(input("1. Bisection\n2. Regula falsi\n3. Newton\n4. Secant\n\nEnter choice: "))
    if ch==1:

        a, b = [float(x) for x in input("Enter interval separated by space: ").split()]
        if (f(a) * f(b)) > 0:
            print("No real roots on this interval")
        else:
            print()
            bisection_method(a,b,f,error,truevalue,roundvalue)

    elif ch==2:

        a, b= [float(x) for x in input("Enter interval separated by space: ").split()]
        if (f(a) * f(b)) > 0:
            print("No real roots on this interval")
        else:
            print()
            regula_falsi_method(a, b, f,error,truevalue,roundvalue)

    elif ch==3:
        a, b= [float(x) for x in input("Enter interval separated by space: ").split()]


        if (sp.N(f(a)) * sp.N(f(b))) > 0:
            print("No real roots on this interval")
        else:
            f_prime = sp.lambdify(x, sp.diff(sp.sympify(str_expression), x))
            print()
            newton_method((a+b)/2,f,f_prime,error,truevalue,roundvalue)

    elif ch==4:
        P0, P1 = [float(x) for x in input("Enter interval separated by space: ").split()]
        if (f(P0) * f(P1)) > 0:
            print("No real roots on this interval")
        else:
            print()
            secant_method(P0, P1, f, error, truevalue,roundvalue)

    choice=str(input("Do you want to continue (Y or N): "))

input()
