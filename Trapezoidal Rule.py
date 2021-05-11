#Function to calculate trapezoidal rule

def Trapezoidal_Rule(f0,f1,h):
    a = h/2
    b = f0 + f1
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

print("Enter value of f(", LowerLimit, ")")
Function_LowerLimit = input()
Function_LowerLimit = float(Function_LowerLimit)

print("Enter value of f(", UpperLimit, ")")
Function_UpperLimit = input()
Function_UpperLimit = float(Function_UpperLimit)

#Getting value of h

h = Calculate_h(UpperLimit , LowerLimit,1)
h = float(h)

#Calling main function for result 

Result = Trapezoidal_Rule(Function_LowerLimit,Function_UpperLimit,h)
Result = float(Result)

print("\n-----------------------------------------------------\n")
print("Integeral of function under the limit [",LowerLimit,",",UpperLimit, "]: " , Result ,"using Trapezoidal Rule")
