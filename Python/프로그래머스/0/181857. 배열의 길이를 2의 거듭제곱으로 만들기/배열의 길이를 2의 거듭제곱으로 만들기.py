def solution(arr):
    n = len(arr)
    
    target_len = 1
    
    while target_len < n:
        target_len*=2
        
    return arr + [0] * (target_len - n)