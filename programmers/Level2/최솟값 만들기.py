def solution(A,B):
    answer = 0
    a_arr, b_arr = sorted(A), sorted(B, reverse=True)
    for i in range(len(A)):
        answer += a_arr[i] * b_arr[i]

    return answer