def solution(ingredient):
    answer = 0
    answer_r = []
    for num in ingredient:
        answer_r.append(num)
        if answer_r[-4:] == [1, 2, 3, 1]:
            answer += 1
            del answer_r[-4:]
    
    return answer