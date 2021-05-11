#Function to calculate trapezoidal rule

def Simpson_Rule(f0,f1,f2,h):
    a = h/3
    b = f0 + (4 * f1) + f2
    return a*b

#Function to calculate value of h

def Calculate_h(b,a,n):
    h = (b-a)/n
    h = float(h)
    return h

#Getting upper limit and lower limit

LowerLimit = input("Enter Lower Limit of the Function: ")
LowerLimit = float(LowerLimit)

UpperLimit = input("Enter Upper Limit of the Function: ")
UpperLimit = float(UpperLimit)

#Getting Function Values
print("Enter value of f(x0)")
Function_UpperLimit = input()
Function_UpperLimit = float(Function_UpperLimit)

#Calculating value of h

h = Calculate_h(UpperLimit , LowerLimit,2)
h = float(h)

#Getting Function Values

print("Enter value of f(x1)")
Function_MiddleLimit = input()
Function_MiddleLimit = float(Function_MiddleLimit)

print("Enter value of f(x2)")
Function_LowerLimit = input()
Function_LowerLimit = float(Function_LowerLimit)

#Calling main function for result 

Result = Simpson_Rule(Function_LowerLimit,Function_MiddleLimit,Function_UpperLimit,h)
Result = float(Result)

print("\n-----------------------------------------------------\n")
print("Integeral of function under the limit [",LowerLimit,",",UpperLimit, "]: " , Result , "using Simspson Rule")
