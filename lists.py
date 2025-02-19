#!/usr/bin/env python

fruits = ["Lemon", "Orange", "Apples","Kiwi","Peaches", "Mangoes","Guavas"]

print(fruits)
fruits[0] = "Bananas"
print(fruits)

fruits[-3]= "Pineapples"
print(fruits)

#for loop tp print all fruits

for fruit in fruits :
    print(fruit)

fruits.append("Water Mellon") 
fruits.append("Lime")
fruits.append("Avocado")
print(fruits)

fruits.pop()
print(fruits)
fruits.insert(3, "Cherry")
print(fruits)
fruits.extend(["Momm", "Tomato", "Sumpt"])
fruits.sort()
print(fruits)