from itertools import *

def solution(nums):
    answers = list(combinations(nums, 3))
    return_count = 0
    for answer in answers:
        count = 0
        for x in range(2, sum(answer)):
            if sum(answer) % x == 0:
                count += 1
        if count == 0:
            return_count += 1

    return return_count