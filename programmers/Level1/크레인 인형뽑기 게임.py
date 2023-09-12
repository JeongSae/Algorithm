def solution(board, moves):
    answer = 0
    board_length = len(board[0])
    transpose_board = [list(x) for x in zip(*board)]
    
    stack_dolls = []
    last_doll = ''
    for move in moves:
        board_index = move - 1
        for length in range(board_length):
            if transpose_board[board_index][length] != 0:
                poped_value = transpose_board[board_index][length]
                transpose_board[board_index][length] = 0
                # 앞 인형 확인
                if last_doll == poped_value:
                    stack_dolls.pop(len(stack_dolls)-1)
                    if len(stack_dolls) > 0:
                        last_doll = stack_dolls[-1]
                    else:
                        last_doll = ''
                    answer += 2
                else:
                    last_doll = poped_value
                    stack_dolls.append(poped_value)
                break
            else:
                continue
    
    return answer