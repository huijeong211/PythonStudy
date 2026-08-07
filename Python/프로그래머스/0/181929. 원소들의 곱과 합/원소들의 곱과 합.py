def solution(num_list):
    
    mul_ans = 1
    sum_ans = 0
    
    for num in num_list:
        
        mul_ans *= num
        sum_ans += num
        
    if mul_ans < (sum_ans ** 2):
        return 1
    else:
        return 0