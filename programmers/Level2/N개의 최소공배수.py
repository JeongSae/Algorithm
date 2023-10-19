from math import gcd

def solution(arr):
    answer = 0
    first_value = arr.pop(0)
    
    while arr:
        second_value = arr.pop(0)
        lcm = first_value * second_value // gcd(first_value, second_value)
        first_value = lcm
    
    return first_value