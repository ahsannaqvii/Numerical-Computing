import os
import numpy as np  

def Div_Diff(y,x,n):
    for i in range(1, n): 
        for j in range(n - i): 
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /  (x[j] - x[i + j]));
    return y;                               
    

def Product(i, value, x):   # Function to find the product term 
    pro = 1; 
    for j in range(i): 
        pro = pro * (value - x[j]); 
    return pro; 

    
def DDTFormula(k,x,y,n):
    sum = y[0][0]; 
  
    for i in range(1, n):
        sum = sum + (Product(i, k, x) * y[0][i]); 
      
    return sum; 

y = [[0 for i in range(7)] 
        for j in range(7)]; #Making 2D array for storing values
 
input_string = input ('Enter the number of observations ')  #Getting the total no of obs
print("\n")
n= int(input_string)
#Inputting values of x and y
input_string = input('Enter elements of a list separated by space(Values of X) ')
print("\n")
x = input_string.split()

for i in range(len(x)):
    x[i] = float(x[i])    


for i in range(n):
    y[i][0]=input('Enter the value of Y')
    y[i][0]=float(y[i][0])

                    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



input_string=input('Enter the true value which you wish to find')#Input the true value
print("\n")
k=float(input_string) #Int conversion

y=Div_Diff(y,x,n)   #This function would return the DDTs'

# printing the value 
print("\nValue at", k, "is",
        round(DDTFormula(k, x, y, n), 7))   #rounding the answer to 7 digits returned by DDTFormula func