def solution(keymap, targets):
    answer = []
    for target in targets:
        num_answer = 0
        for t in target:
            min_index = []
            num_keymap = len(keymap)
            for i in range(num_keymap):
                if t in keymap[i]:
                    min_index.append(keymap[i].index(t)+1)
            if min_index:
                num_answer += min(min_index)
            else:
                num_answer = -1
                break
        answer.append(num_answer)
        
    return answer