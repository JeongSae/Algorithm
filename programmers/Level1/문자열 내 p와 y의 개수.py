def solution(array):
    array = array.lower()
    if array.count('p') == array.count('y'):
        return True
    elif array.count('p') == 0 and array.count('y') == 0:
        return True
    else:
        return False