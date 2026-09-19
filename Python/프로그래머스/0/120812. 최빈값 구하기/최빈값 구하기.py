def solution(array):
    count_dict = {}
    
    for num in array:
        if num in count_dict:
            count_dict[num]+=1
        else:
            count_dict[num]= 1
            
    max_count = max(count_dict.values())
            
    modes = []
    
    for num,count in count_dict.items():
        if count == max_count:
            modes.append(num)
            
        if len(modes) > 1:
            return -1
        
    return modes[0]
            
            
        
        
            