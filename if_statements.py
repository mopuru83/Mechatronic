#!/usr/bin/env python

#program that calculates tax for civil servants

# 0-50000  10% tax
#50001-100000 15% tax
#100000-500000 20% tax
#above 500000 25% tax

#get user in put as salary
salary=float(input("Please enter your current earnings :  "))

if salary <= 50000 :
    tax =(10* salary/100)
    new_salary = salary - tax
elif salary > 50000 and salary < 100000:
    tax = (15 * salary /100)
    new_salary = salary - tax

elif salary > 100000 and salary < 500000:
    tax = (20 * salary /100)
    new_salary = salary - tax

else :

    tax = (25 * salary / 100)
    new_salary = salary - tax

print(f"Your Gross Salary is {salary}")
print(f"Your net Salary is {new_salary}")



