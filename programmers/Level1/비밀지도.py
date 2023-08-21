def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        num_padding_a1, num_padding_a2 = n - len(bin(a1)[2:]), n - len(bin(a2)[2:])
        padded_a1, padded_a2 = '0'*num_padding_a1+bin(a1)[2:], '0'*num_padding_a2+bin(a2)[2:]
        return_array = ''
        for i in range(n):
            if int(padded_a1[i]) + int(padded_a2[i]) > 0:
                return_array += '#'
            else:
                return_array += ' '
        answer.append(return_array)
    
    return answer