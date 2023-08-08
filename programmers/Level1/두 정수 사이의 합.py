def solution(a, b):
    a_num, b_num = min(a, b), max(a, b)
    return sum([i for i in range(a_num, b_num+1)])