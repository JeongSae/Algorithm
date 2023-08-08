def solution(array):
    condition = list(range(1, 10))
    while array:
        num = array.pop()
        if num in condition:
            condition.pop(condition.index(num))
        else:
            continue
    
    return sum(condition)