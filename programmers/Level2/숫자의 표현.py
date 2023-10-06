def solution(n):
    answer = 0
    numbers = list(range(1, n+1))
    for number in numbers:
        sum_value = 0
        for num in range(number, n+1):
            sum_value += num
            if sum_value == n:
                answer += 1
            if sum_value > n:
                break
    
    return answer