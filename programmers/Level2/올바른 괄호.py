def solution(s):
    acc = []
    for i in range(len(s[:])):
        if s[i] == '(':
            acc.append(s[i])
        else:
            if acc:
                acc.pop()
            else:
                return False
            
    if acc:
        return False
    return True