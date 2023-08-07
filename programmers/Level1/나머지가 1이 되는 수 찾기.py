def solution(num):
    for i in range(1, num+1):
        if num % i == 1:
            return i