import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#
#bill: an array of integers representing the cost of each item ordered
#k: an integer representing the zero-based index of the item Anna doesn't eat
#b: the amount of money that Anna contributed to the bill

def bonAppetit(bill, k, b):
    # Write your code here
    subtotal = 0
    total = sum(bill)
    r = [s for idx, s in enumerate(bill) if idx != k]
    subtotal = sum(r) // 2
    total = total // 2
    if subtotal == b:
        print("Bon Appetit")
    else:
        print(total - subtotal)
    

if __name__ == '__main__':
    k = 1
    b = 7
    bill = [3, 10, 2, 9]
    #esperado = 12
    bonAppetit(bill, k, b)