def solution(numbers):
    answer = []
    while numbers:
        pop_num = numbers.pop(0)
        for num in numbers:
            answer.append(pop_num+num)
        
    return sorted(set(answer))