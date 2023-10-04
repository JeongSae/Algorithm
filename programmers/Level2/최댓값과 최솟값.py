def solution(s):
    splited_string = list(map(int, s.split(' ')))
    return '{} {}'.format(min(splited_string), max(splited_string))