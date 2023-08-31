def solution(n):
    answer = 0
    for i in range(2, n+1):
        count = 0
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                count += 1
                break
        if count == 0:
            answer += 1
            
    return answer