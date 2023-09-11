def solution(s):
    s = list(s)
    answer = 0
    main, sub = 1, 0
    main_s = s.pop(0)
    
    for string in s:
        if main == sub:
            answer += 1
            main_s = string
        
        if main_s == string:
            main += 1
        else:
            sub += 1
    
    return answer + 1