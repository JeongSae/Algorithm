def solution(array):
    if len(array) == 1:
        return [-1]
    
    min_value_index = array.index(min(array))
    array.pop(min_value_index)
    
    return array