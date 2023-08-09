def solution(num):
    if num % 2 == 0:
        return '수박'*int(num / 2)
    else:
        return '수박'*(int(num / 2))+'수'