def solution(numbers, value):
    answer = 0
    for i in range(len(numbers)-len(value)+1):
        if int(numbers[i:i+len(value)]) <= int(value):
            answer += 1
    
    return answer