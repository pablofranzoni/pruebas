import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    points = [0,0,0,0,0,0]
    for i in arr:
        points[i] += 1
    max_index = points.index(max(points))
    return max_index

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    print(migratoryBirds(arr))
