def solution(s):
    sorted_string = sorted(s, reverse=True)
    
    return ''.join(sorted_string)