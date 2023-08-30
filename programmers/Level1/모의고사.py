def solution(answers):
    iter_len = len(answers) // 5 + 1
    math_one = ([1, 2, 3, 4, 5] * iter_len)[:len(answers)]
    math_two = ([2, 1, 2, 3, 2, 4, 2, 5] * iter_len)[:len(answers)]
    math_three = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * iter_len)[:len(answers)]
    
    one_cnt, two_cnt, three_cnt = 0, 0, 0
    for one, two, three, answer in zip(math_one, math_two, math_three, answers):
        if one == answer:
            one_cnt += 1
            
        if two == answer:
            two_cnt += 1
            
        if three == answer:
            three_cnt += 1
            
    max_idx = max(one_cnt, two_cnt, three_cnt)
    results = []
    for i, count in enumerate([one_cnt, two_cnt, three_cnt]):
        if count == max_idx:
            results.append(i+1)
    
    return results