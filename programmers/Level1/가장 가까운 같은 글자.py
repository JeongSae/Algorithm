def solution(s):
    answer = []
    string_dict = {}
    for i, string in enumerate(s):
        if string in string_dict:
            string_idx = string_dict[string]
            answer.append(abs(i - string_idx))
            string_dict[string] = i
        else:
            string_dict[string] = i
            answer.append(-1)
        
    return answer