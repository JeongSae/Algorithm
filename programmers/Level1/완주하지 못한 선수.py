from collections import Counter

def solution(participant, completion):
    answer = ''
    p_c, c_c = Counter(participant), Counter(completion)
    value = p_c - c_c
    return list(value.keys())[0]