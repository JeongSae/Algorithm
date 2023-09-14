def solution(numbers, hand):
    answer = ''
    left_nums, right_nums, other_nums = [1, 4, 7], [3, 6, 9], [2, 5, 8, 0]
    left_coor, right_coor = [3, 0], [3, 2]
    for num in numbers:
        if num == 0:
            num_coor = [3, 1]
        elif num < 4 :
            num_coor = [0, num-1]
        else:
            num_coor = [int((num-1) / 3), (num-1) % 3]
            
        if num in left_nums:
            answer += 'L'
            left_coor = num_coor
        elif num in right_nums:
            answer += 'R'
            right_coor = num_coor
        elif num in other_nums:
            sub_left = sum([abs(num_coor[0] - left_coor[0]), abs(num_coor[1] - left_coor[1])])
            sub_right = sum([abs(num_coor[0] - right_coor[0]), abs(num_coor[1] - right_coor[1])])
            if sub_left < sub_right:
                answer += 'L'
                left_coor = num_coor
            elif sub_left > sub_right:
                answer += 'R'
                right_coor = num_coor
            elif sub_left == sub_right and hand == 'right':
                answer += 'R'
                right_coor = num_coor
            elif sub_left == sub_right and hand == 'left':
                answer += 'L'
                left_coor = num_coor
    
    return answer