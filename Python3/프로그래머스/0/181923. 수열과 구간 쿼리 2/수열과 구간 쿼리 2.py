def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        candidates = []
        
        for i in range(s, e+1):
            if arr[i] > k:
                candidates.append(arr[i])
                
        if len(candidates) == 0:
            answer.append(-1)
            
        else:
            answer.append(min(candidates))
    return answer