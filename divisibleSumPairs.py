import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    t = 0
    for i in range(n):
        for j in range(i+1,n):
            #print(ar[i], ar[j], sep=",")
            if (ar[i] + ar[j]) % k == 0:
                t += 1
    return t

if __name__ == '__main__':
    ar = [1,3,2,6,1,2]
    n = 6
    k = 3
    print(divisibleSumPairs(n, k, ar))