import os
import numpy as np  

def calculateS(s,val):
    temp = s;
    for i in range(1, val):
        temp = temp * (s - i);
    return temp;

# Calculate Factorial
def calFact(n):
    fact = 1;
    for i in range(2, n + 1):
        fact *= i;
    return fact;
 
print("\t\tNOTE : PLEASE ENTER THE VALUES IN FLOAT");
input_string = input ('Enter the number of observations ')  #Getting the total no of obs
print("\n")
n= int(input_string)

input_string = input('Enter elements of a list separated by space(Values of X) ') #Inputting values of x 
print("\n")
x = input_string.split()    #Splling input_string by spaces

for i in range(len(x)):
    x[i] = float(x[i])        #Conversion into int

y = [[0 for i in range(7)] 
        for j in range(7)]; #Making 2D array for storing values

for i in range(n):
    y[i][0]=input('Enter the value of Y')   #Inputting values of  y
    y[i][0]=float(y[i][0])

                    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



input_string=input('Enter the true value which you wish to interpolate\n')  #Input the true value
k=float(input_string) #Int conversion


for i in range(1, n):
    for j in range(n - i):  # Calculating the forward difference table
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
 

for i in range(n):
    print(x[i], end = "\t");
    for j in range(n - i):
        print(y[i][j], end = "\t"); # Displaying the forward difference table
    print("");

equationSum=y[0][0];    #F(x)   
s=(k-x[0]) / ( x[1]-x[0] ) #initial S value
for i in range(1,n):
    equationSum = equationSum + (calculateS(s, i) * y[0][i]) / calFact(i);
 
print("\nValue at", k,
      "is", round(equationSum, 8));
