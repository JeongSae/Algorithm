def solution(n):
    fibonacci = [0, 1]
    for i, num in enumerate(range(2, n+1)):
        num_idx_1, num_idx_2 = num-2, num-1
        next_value = fibonacci[num_idx_1] + fibonacci[num_idx_2]
        fibonacci.append(next_value)
    
    return fibonacci[n] % 1234567