import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    months = [31,28,31,30,31,30,31,31]
    if year == 1918:
        months[1] -= 13
    elif year < 1919 and year % 4 == 0:
        months[1] += 1
    else:
        if year % 400 == 0: months[1] += 1
        if year % 4 == 0 and year % 100 != 0: months[1] += 1
    days_sum = sum(months)
    day = 256 - days_sum
    return str(day) + ".09." + str(year)

if __name__ == '__main__':
    print(dayOfProgrammer(1800))