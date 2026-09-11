def solution(picture, k):
    result = []
    for row in picture:
        
        new_row = ""
        for char in row:
            new_row += char * k
        
        
        for _ in range(k):
            result.append(new_row)
            
    return result