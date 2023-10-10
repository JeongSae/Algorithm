def solution(s):
    stacks = []
    for i, string in enumerate(s):
        if i == 0 or len(stacks) == 0:
            stacks.append(string)
            continue
        
        if stacks[-1] == string:
            stacks.pop(-1)
        else:
            stacks.append(string)
            
    if stacks:
        return 0
    else:
        return 1