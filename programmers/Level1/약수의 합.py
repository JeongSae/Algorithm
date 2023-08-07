def solution(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += i
        else:
            continue
    return cnt