def solution(n, words):
    answer = {}
    answer_person = {}
    lose, last_word = False, ''
    for word in words:
        answer[word] = 0
        
    for person in range(n):
        answer_person[person] = 0
        
    iter_count = 0
    for i_n, word in enumerate(words):
        # 순서 초기화
        if iter_count == n:
            iter_count = 0
            
        # 순서 카운팅
        answer_person[iter_count] += 1
        answer[word] += 1
        
        # 단어 카운팅 및 끝자리 맞는지
        if i_n > 0:
            if last_word[-1] != word[0]:
                lose = True
                break
            
        if answer[word] > 1:
            lose = True
            break
        
        iter_count += 1
        last_word = word
    
    if lose == False:
        return [0, 0]
    else:
        return [iter_count+1, answer_person[iter_count]]