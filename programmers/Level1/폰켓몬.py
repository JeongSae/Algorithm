def solution(nums):
    set_nums = set(nums)
    return min(len(set_nums), int(len(nums) / 2))