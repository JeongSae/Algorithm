import math

def solution(num):
    result = math.sqrt(num)
    if result % 1 == 0:
        return (int(result)+1)**2
    else:
        return -1