def solution(name, yearning, photo):
    answer = []
        
    for s_photo in photo:
        cnt = 0
        for s_name, s_year in zip(name, yearning):
            if s_name in s_photo:
                cnt += s_photo.count(s_name) * s_year
        answer.append(cnt)
            
    return answer