def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    win_count = 0
    while len(lottos) != 0:
        number = lottos.pop()
        if number in win_nums:
            win_count += 1
    
    if zero_count == 6:
        return [1, 6]
    
    if win_count == 6:
        return [1, 1]
    
    if win_count == 0 and zero_count == 0:
        return [6, 6]
        
    return [7-(win_count+zero_count), 7-win_count]