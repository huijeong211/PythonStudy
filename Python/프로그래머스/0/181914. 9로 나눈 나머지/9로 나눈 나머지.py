def solution(number):
    total_sum = 0
    
    for digit in number:
        total_sum += int(digit)
        
    return total_sum % 9