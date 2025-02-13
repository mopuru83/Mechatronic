#!/usr/bin/env python

weight = int(input("Weight:   "))
unit =input("(L)Pounds or (K) Kgs")

if unit.upper()== "L":
  converted_weight = weight*0.45
  print("You are {converted_weight} kilos")          
else:
  unit.upper()== "K"
  converted_weight= weight/0.45

  print(f"You are {converted_weight} pounds")   
