def solution(string):
    if len(string) % 2 == 0:
        return string[int(len(string) / 2)-1:int(len(string) / 2)+1]
    else:
        return string[int(len(string) / 2)]