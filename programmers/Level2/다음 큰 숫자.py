def solution(n):
    count = 1
    target = bin(n)[2:].count('1')
    while True:
        if bin(n+count)[2:].count('1') == target:
            break
        
        count += 1
        
    return n+count