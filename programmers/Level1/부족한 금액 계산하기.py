def solution(price, money, count):
    result = 0
    for i in range(1, count+1):
        result += int(price*i)
    
    if result > money:
        return result - money
    else:
        return 0