def solution(string, num):
    answer = ''
    for i, s in enumerate(string):
        if int(num / 26) < 2:
            sub_num = 26
        else:
            sub_num = int(26 * int(num / 26))
        
        if s.islower():
            if ord(s) + num > 122:
                answer += chr(ord(s) + num - sub_num)
            else:
                answer += chr(ord(s) + num)
        elif s.isupper():
            if ord(s) + num > 90:
                answer += chr(ord(s) + num - sub_num)
            else:
                answer += chr(ord(s) + num)
        else:
            answer += ' '
    
    return answer