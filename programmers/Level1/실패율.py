def solution(N, stages):
    answer = {}
    remain_num = len(stages)
    remain_count = 0
    for stage in range(1, N+1):
        count = 0
        for in_stage in stages:
            if in_stage <= stage:
                count += 1
                
        if remain_num - remain_count == 0:
            answer[stage] = 0.0
        else:
            answer[stage] = (count - remain_count) / (remain_num - remain_count)
            remain_count = count
        
    sorted_dict = sorted(answer.items(), key=(lambda x: x[1]), reverse=True)
    return [x[0] for x in sorted_dict]