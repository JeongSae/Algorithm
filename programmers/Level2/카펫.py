def solution(brown, yellow):
    answer = []
    total_tile = brown + yellow
    total_div = 0
    for i in range(3, total_tile):
        if total_tile // i < i:
            break
        answer.append([total_tile // i, i])
        
    submit_answer = []
    for i, j in answer:
        if (i-2) * (j-2) == yellow:
            submit_answer.append(i)
            submit_answer.append(j)
            break
    
    return submit_answer