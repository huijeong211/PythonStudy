def solution(num_list):
    last = num_list[-1]
    prev = num_list[-2]
    
    if last > prev:
        new_value = last - prev
    
    else:
        new_value = last * 2
        
    num_list.append(new_value)
    
    return num_list