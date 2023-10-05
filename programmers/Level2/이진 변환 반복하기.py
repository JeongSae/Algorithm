def clear_zero(s):
    answer = ''
    num_zero = 0
    for string in s:
        if string == '0':
            num_zero += 1
            continue
        else:
            answer += string
    return answer, num_zero

def get_bin(s):
    return str(bin(len(s))[2:])

def solution(s):
    del_zero_cnt, t_bin_cnt = 0, 0
    while s != '1':
        s, zeros = clear_zero(s)
        s = get_bin(s)
        
        del_zero_cnt += zeros
        t_bin_cnt += 1
    
    return [t_bin_cnt, del_zero_cnt]