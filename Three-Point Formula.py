#Initializing Arrays

ValuesOf_x = []
ValuesOf_fx = []

#Function to calculate Three Point Mid Point

def ThreePoint_MidPoint(x0,h):
    a = f(x0+h)
    a = float(a)
    b = f(x0-h)
    b = float(b)
    # (f(x0+h)-f(x0-h)/2*h)
    return (a-b)/(2*h) 

#Function to calculate Three Point End Point

def ThreePoint_EndPoint(x0,h):
    a = f(x0) * -3
    a = float(a)
    b = 4 * f(x0+h)
    b = float(b)
    c = f(x0 + 2*h)
    c = float(c)
    return (a+b-c)/(2*h)          

#Function to get the value of the function on the corresponding x 

def f(x):
    x = round(x,2)
    for i in range(TotalNumOfValues):
        # print("Value of x: ",ValuesOf_x[i])
        if x == ValuesOf_x[i]:
            return ValuesOf_fx[i]
    return 0

#Getting total number of values of x for table 

TotalNumOfValues = input("Enter total number of values of x: ")
TotalNumOfValues = int(TotalNumOfValues)
print(TotalNumOfValues)

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
        Result = ThreePoint_EndPoint(x0,h)
        Result = round(Result,6)
    elif ((x0 != ValuesOf_x[0]) and (x0 != ValuesOf_x[TotalNumOfValues-1])):         #Five-Pont MidPoint
        Result = ThreePoint_MidPoint(x0,h)
        Result = round(Result,6)
    elif ((x0 == ValuesOf_x[TotalNumOfValues-1])):                                   #Five-Point EndPoint
        Result = Result = ThreePoint_EndPoint(x0,(h*-1))
        Result = round(Result,6)
    print("\n-----------------------------------------------------\n")
    print("f'(",x0,"): ",Result)

    print("\nDo you wish to continue? \n1.Yes \n2.No")
    Option = input()
    Option = int(Option)