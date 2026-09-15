def solution(n):
    arr = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n-1
    left, right = 0, n-1
    
    num =1
    
    while num <= n*n:
        # 왼 오
        for j in range(left, right +1 ):
            arr[top][j] = num
            num += 1
        top +=1
        
        #위 아래
        for i in range(top, bottom+1):
            arr[i][right] = num
            num += 1
        right -= 1
        
        #오 왼
        for j in range(right, left -1,-1):
            arr[bottom][j] = num
            num += 1
        bottom -= 1
        
        # 아래 위
        for i in range(bottom, top -1, -1):
            arr[i][left] = num
            num += 1
        left += 1
    
    
    return arr