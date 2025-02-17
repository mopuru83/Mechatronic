#!/usr/bin/env python

import sys

n = len(sys.argv)

print(n)                  #prints the number of strings
print(sys.argv[0])        # prints the first item
print(sys.argv[1])         # prints the second item
print(sys.argv[2])          # prints the third item


sum =0

for i in range(1, n):
    sum=sum + int(sys.argv[i])
print(sum)