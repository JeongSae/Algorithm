def solution(new_id):
    answer = ''
    strings = 'qwertyuiopasdfghjklzxcvbnm0123456789-_.'
    com_list = ['.'*i for i in range(16, 1, -1)]
    lower_id = new_id.lower()
    for id_str in lower_id:
        if id_str not in strings:
            lower_id = lower_id.replace(id_str, '')
            
    for com in com_list:
        if com in lower_id:
            lower_id = lower_id.replace(com, '.')
            
    if lower_id[0] == '.':
        lower_id = lower_id[1:]
        
    if len(lower_id) == 0:
        lower_id += 'a'
    
    if lower_id[-1] == '.':
        lower_id = lower_id[:-1]
        
    if len(lower_id) > 15:
        lower_id = lower_id[:15]
    
    if lower_id[-1] == '.':
        lower_id = lower_id[:-1]
        
    while len(lower_id) < 3:
        lower_id += lower_id[-1]
    
    return lower_id