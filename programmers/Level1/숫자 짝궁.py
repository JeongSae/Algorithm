from collections import Counter

def solution(X, Y):
    answer = ''
    
    counted_x, counted_y = Counter(str(X)), Counter(str(Y))
    for i_value in range(9, -1, -1):
        answer += (str(i_value) * min(counted_x[str(i_value)], counted_y[str(i_value)]))
    
    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer