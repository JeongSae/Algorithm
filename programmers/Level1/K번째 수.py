def solution(array, commands):
    answer = []
    for com in commands:
        sorted_array = sorted(array[com[0]-1:com[1]])
        if len(sorted_array) < com[2]:
            answer.append(sorted_array[0])
        else:
            answer.append(sorted_array[com[2]-1])
    return answer