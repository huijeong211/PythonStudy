def solution(num_list):
    even_count = 0  # 짝수 개수
    odd_count = 0   # 홀수 개수
    
    for num in num_list:
        if num % 2 == 0:  # 2로 나누어 떨어지면 짝수
            even_count += 1
        else:             # 아니면 홀수
            odd_count += 1
            
    return [even_count, odd_count]