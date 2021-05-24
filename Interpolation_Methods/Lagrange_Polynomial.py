import os

input_string = input('Enter elements of a list separated by space(Values of X) ')   #Inputting Values of X in string
print("\n")
x_Values = input_string.split() #Splitting String into portions by Space

for i in range(len(x_Values)):
    x_Values[i] = int(x_Values[i])    #Int conversion

input_string = input('Enter elements of a list separated by space(Values of Y) ') #Inputting Values of Y in string
print("\n")
y = input_string.split()    #Splitting String into portions by Space

for i in range(len(y)):
    y[i] = float(y[i])  #for conversion into int


n=len(x_Values) -1 #Degree of Polynomial
yp=0
input_string = input('Enter the true value which you wish to find.\n ') #Input the true value
print("\n")
True_Value=int(input_string)    #Int Conversion



for i in  range(n+1):
    p=1 #Polynomial value taken as 1 to multiply it
    for j in range(n+1):
        if j!=i:     #base condition 
            p*=(True_Value-x_Values[j])/(x_Values[i]-x_Values[j])   
    yp+=y[i]*p #Multiply function value with the polynomial (L0.f(x0)) + (L1.f(x1))

print("For True value of X : %.5f, y=%.5f" % (True_Value,yp))   #Displaying Answers.