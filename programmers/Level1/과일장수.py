def solution(k, m, score):
    answer = 0
    num_boxes = len(score) // m
    sorted_score = sorted(score, reverse=True)
    for i in range(num_boxes):
        get_score = sorted_score[i*m:(i+1)*m]
        answer += min(get_score) * m
        
    return answer