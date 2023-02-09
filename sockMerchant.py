import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar_sorted = sorted(ar)
    ult_elem = 0
    count_pair = 0
    j = 0
    for elem in ar_sorted:
        print(elem)
        if elem != ult_elem:
            ult_elem = elem
            j = 0
        else:
            if j % 2 == 0:   
                count_pair += 1
            j += 1
    return count_pair


if __name__ == '__main__':
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]  #3 pares
    ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5] #9 pares
    n = len(ar)
    result = sockMerchant(n, ar)
    print(result)
