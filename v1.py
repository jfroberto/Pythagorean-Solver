import math
from math import sqrt

print ('Pyhtagorean Theoream')
print ('     *  ')
print ('   * *  ')
print ('C *  * B')
print (' *   *  ')
print ('******  ')
print ('   A    ')

print ('Which side is missing: ')
missing = input('Type which side is Missing: ')

if missing == 'A':
    num_B = input('Enter side B: ')
    num_C = input('Enter Side C: ')
    num_A= math.sqrt ((-float(num_B)**2) + (float(num_C)**2))
    print (num_A)

elif missing == 'B':
    num_A = input('Enter side A: ')
    num_C = input('Enter Side C: ')
    num_B = sqrt( (float(num_C) ** 2) - (float(num_A) ** 2))
    print(num_B)

elif missing == 'C':
    num_A = input('Enter side A: ')
    num_B = input('Enter Side B: ')
    num_C = sqrt((float(num_A) ** 2) + (float(num_B) ** 2))
    print(num_C)

print('Please press Enter')
