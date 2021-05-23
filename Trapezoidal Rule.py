#  --------------------------------- 
# | Chapter 4: Trapezoidal Rule     |
#  ---------------------------------


#Function to calculate trapezoidal rule

import msvcrt

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

LowerLimit = input("\nEnter Lower Limit of the Function: ")
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
print(" x \t|\t f(x)")
print(LowerLimit ,"\t|\t" , Function_LowerLimit)
print(UpperLimit , "\t|\t" , Function_UpperLimit)
print("\nIntegeral of function under the limit [",LowerLimit,",",UpperLimit, "]: " , Result ,"using Trapezoidal Rule")

char = msvcrt.getch()
# Test Case 1

# Enter Lower Limit of the Function: 0.5
# Enter Upper Limit of the Function: 1
# Enter value of f( 0.5 )
# 0.0625
# Enter value of f( 1.0 )
# 1