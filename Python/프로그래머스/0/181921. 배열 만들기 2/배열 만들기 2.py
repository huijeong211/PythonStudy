def solution(l, r):
    answer = []
    
    for num in range(l, r + 1):
        num_set = set(str(num))
        
        if num_set.issubset({"0","5"}):
            answer.append(num)
            
    if len(answer) == 0:
        return [-1]
            
    return answer