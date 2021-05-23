#  ---------------------------------
# | Chapter 4: Five-Point Formula   |
#  ---------------------------------

#Initializing Arrays

ValuesOf_x = []
ValuesOf_fx = []

#Function to calculate Five Point Mid Point

def FivePoint_MidPoint(x0,h):
    a = f(x0-(2*h))  
    a = float(a)
    b = 8*(f(x0-h))
    b = float(b)
    c = 8*(f(x0+h))
    c = float(c)
    d = f(x0+(2*h))
    d = float(d)
    return (a-b+c-d) / (12 * h) 

#Function to calculate Five Point End Point

def FivePoint_EndPoint(x0,h):
    a = 25 * f(x0)  
    a = float(a)
    b = 48 * (f(x0+h))
    b = float(b)
    c = 36 * (f(x0+ (2*h)))
    c = float(c)
    d = 16 * f(x0+(3*h))
    d = float(d)
    e = 3 * f(x0+(4*h))
    e = float(e)
    return (-a+b-c+d-e) / (12 * h)          # 1/12h [-25f(x0)+48f(x0+h)-36f(x0+2h)+16f(x0+3h)-3f(x0+4h)]

#Function to get the value of the function on the corresponding x 

def f(x):
    x = round(x,2)
    for i in range(TotalNumOfValues):
        if x == ValuesOf_x[i]:
            return ValuesOf_fx[i]
    return 0

#Getting total number of values of x for table 

TotalNumOfValues = input("\nEnter total number of values of x: ")
TotalNumOfValues = int(TotalNumOfValues)

#Getting values of x and f(x) for table 

print("\nFOR TABLE CREATION: \n")

for i in range(TotalNumOfValues):
    print("Enter Value of x",i+1)
    val = input("")
    ValuesOf_x.append(val)
    print("Enter Value of f(x",i+1,")")
    val = input("")
    ValuesOf_fx.append(val)
    ValuesOf_x[i] = float(ValuesOf_x[i])
    ValuesOf_fx[i] = float(ValuesOf_fx[i])

#Getting value of x0 

Option = 1

while(Option == 1):
    x0 = input("Enter the value of x0: ")
    x0 = float(x0)

    #Getting value of h 

    h = input("Enter the value of h: ")
    h = float(h)

    if (x0 == ValuesOf_x[0]):                                                        #Five-Point EndPoint 
        Result = FivePoint_EndPoint(x0,h)
        Result = round(Result,6)
    elif ((x0 != ValuesOf_x[0]) and (x0 != ValuesOf_x[TotalNumOfValues-1])):         #Five-Pont MidPoint
        Result = FivePoint_MidPoint(x0,h)
        Result = round(Result,6)
    elif ((x0 == ValuesOf_x[TotalNumOfValues-1])):                                   #Five-Point EndPoint
        Result = Result = FivePoint_EndPoint(x0,(h*-1))
        Result = round(Result,6)

    print("\n-----------------------------------------------------\n")
    print(" x \t\t  f(x)")
    for i in range(TotalNumOfValues):
        print(ValuesOf_x[i] , "\t|\t" , ValuesOf_fx[i])

    print("\nf'(",x0,"): ",Result)

    print("\nDo you wish to continue? \n1.Yes \n2.No")
    Option = input()
    Option = int(Option)

# Test Case 1

# Enter total number of values of x: 6
# Enter Value of x 1
# -3.0
# Enter Value of f(x 1 )
# 9.367879
# Enter Value of x 2
# -2.8
# Enter Value of f(x 2 )
# 8.233241
# Enter Value of x 3
# -2.6
# Enter Value of f(x 3 )
# 7.180350
# Enter Value of x 4
# -2.4
# Enter Value of f(x 4 )
# 6.209329
# Enter Value of x 5
# -2.2
# Enter Value of f(x 5 )
# 5.320305
# Enter Value of x 6
# -2.0
# Enter Value of f(x 6 )
# 4.513417
# Enter the value of x0: -2.2
# Enter the value of h: 0.2