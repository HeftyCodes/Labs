# Name: Kenny Almanza
# Date: 01-28-23
# File: LAB01_Almanza.py
# Purpose: Basic calculator functionality in Python
# _   _       __ _         
#| | | | ___ / _| |_ _   _ 
#| |_| |/ _ \ |_| __| | | |
#|  _  |  __/  _| |_| |_| |
#|_| |_|\___|_|  \__|\__, |
#                    |___/ 
def divide(x,y):
    return x/y
print("Python Calculator")
print("1 Addition")
print("2 Addition")
print("3 Multipication")
print("4 Division")
choice = input ("Enter Your Choice:")
num1 = float (input ("Enter Number 1:"))
num2 = float (input("Enter Number 2:"))
if choice == "1":
    print (num1,"+",num2,"=",(num1+num2))
elif choice == "2":
    print(num1,"-",num2,"=",(num1-num2))
elif choice =="3":
    print (num1,"*",num2,"=",(num1*num2))
elif choice == "4":
    if num2 == 0.0:
        print("Divide By Zero Error")
    else:
        print(num1,"/",num2,"=",(num1/num2))