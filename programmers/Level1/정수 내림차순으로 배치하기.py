def solution(num):
    in_list = [int(i) for i in str(num)]
    sorted_list = sorted(in_list, reverse=True)
    
    text = str(sorted_list[0])
    for i in sorted_list[1:]:
        text += str(i)
    
    return int(text)