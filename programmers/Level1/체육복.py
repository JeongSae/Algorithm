def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    for remain in reserve[:]:
        if remain in lost:
            reserve.remove(remain)
            lost.remove(remain)
            
    for remain in reserve:     
        if remain-1 in lost:
            lost.remove(remain-1)
        elif remain+1 in lost:
            lost.remove(remain+1)
        
    return n - len(lost)