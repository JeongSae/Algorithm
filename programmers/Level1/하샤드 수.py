def solution(num):
    split_num = list(str(num))
    sum_num = sum(map(int, split_num))
    
    if num % sum_num == 0:
        return True
    else:
        return False