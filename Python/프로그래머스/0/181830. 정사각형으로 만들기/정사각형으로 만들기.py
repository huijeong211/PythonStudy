def solution(arr):
    row_count = len(arr)
    cols = len(arr[0])
    
    if row_count > cols:
        for row in arr:
            while len(row) < row_count:
                row.append(0)
                
    elif cols > row_count:
        while len(arr) < cols:
            arr.append([0]*cols)
                
                    
    
    return arr