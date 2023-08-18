def solution(numbers):
    answer = 0
    
    while numbers:
        num = numbers.pop()
        for i, second_num in enumerate(numbers):
            for third_num in numbers[i+1:]:
                if int(num + second_num + third_num) == 0:
                    answer += 1
    
    return answer