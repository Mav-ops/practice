from functools import reduce

def average(lyst):
    Sum = reduce(lambda x, y: x + y, lyst)
    return Sum / len(lyst)

print(average([1, 2, 3, 4]))