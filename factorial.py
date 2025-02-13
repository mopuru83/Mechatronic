#!/usr/bin/env python

#program to calculate factorial of a number using while loop

number = int(input("Enter the number : "))     # Please prompt the user

fact_n =1  #factorial of n

while number >= 1 :
    
    fact_n =number * fact_n      #same as n! = n (n-1)
    number = number -1           #same as n-1
print(fact_n)
