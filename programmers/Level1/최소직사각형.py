def solution(array):
    left_max_value, right_max_value = 0, 0
    for i in range(len(array)):
        sorted_values = sorted(array[i])
        if i == 0:
            left_max_value, right_max_value = sorted_values[0], sorted_values[1]
        else:
            left_max_value, right_max_value = max(left_max_value, sorted_values[0]), max(right_max_value, sorted_values[1])
    
    return left_max_value * right_max_value