def solution(string):
    alphabet_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    match_number = list(range(0, 10))
    
    for num, alphabet in zip(match_number, alphabet_list):
        if alphabet in string:
            string = string.replace(alphabet, str(num))
            print(string)
    
    return int(string)