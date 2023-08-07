def solution(num):
    results = []
    for i in range(1, len(str(num))+1):
        results.append(int(str(num)[-i]))
    
    return results