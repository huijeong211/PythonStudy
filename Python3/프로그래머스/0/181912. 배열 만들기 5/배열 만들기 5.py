def solution(intStrs, k, s, l):
    answer = []
    
    for st in intStrs:
        sub_str = st[s:s+l]
        num = int(sub_str)
        
        if num > k:
            answer.append(num)
    
    return answer