def get_divisor(number):
    count = 0
    for num in range(1, int(number**(1/2))+1):
        if number % num == 0:
            count += 1
            if (num != (number // num)): 
                count += 1
    
    return count

def solution(number, limit, power):
    answer = []
    for num in range(1, number+1):
        div_num = get_divisor(num)
        if div_num > limit:
            answer.append(power)
        else:
            answer.append(div_num)
    return sum(answer)