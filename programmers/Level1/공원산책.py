def solution(park, routes):
    max_w, max_h = len(park[0]), len(park)
    start = [int(''.join(park).index('S') / max_h), ''.join(park).index('S') % max_w]
    operation = {'E' : [0, 1], 'W' : [0, -1], 'N' : [-1, 0], 'S' : [1, 0]}
    temp_start = start
    for move in routes:
        direction, num_step = move.split(' ')
        get_op = operation[direction]
        reset = start
        
        num_x, num_error = 0, 0
        for _ in range(int(num_step)):
            temp_start = temp_start[0] + get_op[0], temp_start[1] + get_op[1]
            
            if temp_start[0] < 0 or temp_start[1] < 0 or temp_start[0] > max_h-1 or temp_start[1] > max_w-1:
                num_error += 1
                break
                
            if temp_start[0] >= 0 and temp_start[1] >= 0:
                if park[temp_start[0]][temp_start[1]] == 'X':
                    num_x += 1
                    break
                    
        if num_error != 0 or num_x != 0:
            temp_start = reset
            continue
            
        start = temp_start
        
    return [start[0], start[1]]