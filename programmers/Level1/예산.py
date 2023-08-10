def solution(arr, budget):
    cnt = 0
    for i in range(len(arr)):
        min_index = arr.index(min(arr))
        pop_min_value = arr.pop(min_index)
        budget -= pop_min_value
        if budget >= 0:
            cnt += 1
        else:
            return cnt
        
    return cnt