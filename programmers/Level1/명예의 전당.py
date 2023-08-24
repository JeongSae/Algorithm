def solution(k, score):
    answer = []
    results = []
    for target_score in score:
        if len(answer) < k:
            answer.append(target_score)
        elif min(answer) < target_score:
            answer.pop(answer.index(min(answer)))
            answer.append(target_score)
        
        results.append(min(answer))
    
    return results