def solution(n):
    composite_count = 0
    
    for i in range(1,n+1):
        divorsors = 0
        
        for j in range(1,i+1):
            if i % j == 0:
                divorsors += 1
                
        if divorsors >= 3:
            composite_count += 1
    
    
    return composite_count