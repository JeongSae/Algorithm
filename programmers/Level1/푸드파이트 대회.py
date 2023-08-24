def solution(food):
    answer = ''
    for i, f_num in enumerate(food[1:]):
        answer += str(i+1) * int(f_num/2)
    reversed_answer = reversed(list(answer))
    reversed_answer = ''.join(reversed_answer)
    return answer+'0'+reversed_answer