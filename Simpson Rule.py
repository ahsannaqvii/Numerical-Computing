#  --------------------------------- 
# | Chapter 4: Simpson Rule         |
#  ---------------------------------

#Function to calculate trapezoidal rule

import msvcrt

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

LowerLimit = input("\nEnter Lower Limit of the Function: ")
LowerLimit = float(LowerLimit)

UpperLimit = input("Enter Upper Limit of the Function: ")
UpperLimit = float(UpperLimit)

#Getting Function Values
print("Enter value of f(x0)")
Function_LowerLimit = input()
Function_LowerLimit = float(Function_LowerLimit)

#Calculating value of h

h = Calculate_h(UpperLimit , LowerLimit,2)
h = float(h)

#Getting Function Values

print("Enter value of f(x1)")
Function_MiddleLimit = input()
Function_MiddleLimit = float(Function_MiddleLimit)

print("Enter value of f(x2)")
Function_UpperLimit = input()
Function_UpperLimit = float(Function_UpperLimit)

#Calling main function for result 

Result = Simpson_Rule(Function_LowerLimit,Function_MiddleLimit,Function_UpperLimit,h)
Result = float(Result)

print("\n-----------------------------------------------------\n")
print(" x \t|\t f(x)")
print(LowerLimit ,"\t|\t" , Function_LowerLimit)
print(h ,"\t|\t" , Function_MiddleLimit)
print(UpperLimit , "\t|\t" , Function_UpperLimit)
print("\nIntegeral of function under the limit [",LowerLimit,",",UpperLimit, "]: " , Result , "using Simspson Rule")
char = msvcrt.getch()

# Test Case 1

# Enter Lower Limit of the Function: 0  
# Enter Upper Limit of the Function: 0.5
# Enter value of f(x0)
# -0.5
# Enter value of f(x1)
# -0.5333333
# Enter value of f(x2)
# -0.5714285