import operator

def solution(survey, choices):
    answer = ''
    scores = [3, 2, 1, 0, 1, 2, 3]
    category = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for sur, cho in zip(survey, choices):
        left, right, number = sur[0], sur[1], cho-1
        if number > 3:
            category[right] += scores[number]
        elif number < 3:
            category[left] += scores[number]
        else:
            continue
            
    category_to_list = list(category.items())
    for i in range(4):
        if category_to_list[i*2:(i+1)*2][0][1] > category_to_list[i*2:(i+1)*2][1][1]:
            answer += category_to_list[i*2:(i+1)*2][0][0]
        elif category_to_list[i*2:(i+1)*2][0][1] < category_to_list[i*2:(i+1)*2][1][1]:
            answer += category_to_list[i*2:(i+1)*2][1][0]
        else:
            string = sorted([category_to_list[i*2:(i+1)*2][0][0], category_to_list[i*2:(i+1)*2][1][0]])[0]
            answer += string
    
    return answer