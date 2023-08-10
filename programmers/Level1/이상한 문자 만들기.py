def solution(string):
    results = []
    
    for string_splited in string.split(' '):
        result_string = ''
        for i in range(len(string_splited)):
            if i % 2 == 0:
                result_string += string_splited[i].upper()
            else:
                result_string += string_splited[i].lower()
        results.append(result_string)
    return ' '.join(results)