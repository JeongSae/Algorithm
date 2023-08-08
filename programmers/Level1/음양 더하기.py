def solution(array, sign):
    sum_num = 0
    for i in range(len(sign)):
        if sign[i]:
            sum_num += array[i]
        else:
            sum_num -= array[i]
    
    return sum_num