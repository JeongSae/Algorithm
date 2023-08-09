def solution(string):
    if len(string) != 4 and len(string) != 6:
        return False
    
    check_list = list(map(str, range(10)))
    for char in string:
        if char not in check_list:
            return False
    
    return True