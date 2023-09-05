def solution(babbling):
    answer = ["aya", "ye", "woo", "ma"]
    count = 0
    for i, word in enumerate(answer):
        for j, say in enumerate(babbling):
            if word in say:
                babbling[j] = babbling[j].replace(word, '{}'.format(i))
    
    for bab in babbling:
        if bab.isnumeric() and len(bab) > 1:
            counting = 0
            for i in range(len(bab)-1):
                if bab[i] == bab[i+1]:
                    counting += 1
            if counting == 0:
                count += 1
                    
        elif bab.isnumeric():
            count += 1
    
    return count