import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d la suma
#  3. INTEGER m largo
#

def birthday(s, d, m):
    # Write your code here
    suma = 0
    k = 0
    for n in range(len(s)-m+1):
        suma = 0
        print()
        for p in range(n,n+m):
            print(p, end=",")
            suma += s[p]
        print("suma ", suma)
        if suma == d:
            k += 1
    return k

if __name__ == '__main__':
    #salida esperada := 3
    #s = [2,2,1,3,2]
    #s = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1] #18, 7
    s = [1, 2, 1, 3, 2] #3, 2
    print(birthday(s,3,2))

