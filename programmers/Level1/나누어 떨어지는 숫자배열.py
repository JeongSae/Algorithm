def solution(array, div):
    results = []
    for i in array:
        if i % div == 0:
            results.append(i)
            
    if results:
        return sorted(results)
    else:
        return [-1]