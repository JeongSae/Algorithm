def solution(n, m, section):
    answer = 1
    first = section[0]
    for i in section[1:]:
        if i < (first+m):
            continue
        else:
            first = i
            answer += 1
            
    return answer