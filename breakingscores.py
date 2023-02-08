import sys

def breakingRecords(scores):
    # Write your code here
    min_b = sys.maxsize
    max_b = - sys.maxsize - 1
    max_bc = 0
    min_bc = 0
    for score in scores:
        if score > max_b:
            max_b = score
            max_bc += 1
        if score < min_b:
            min_b = score
            min_bc += 1
    return [max_bc-1, min_bc-1]

if __name__ == '__main__':
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    print(breakingRecords(scores))
    #esperado 2 4

