def solution(order):
    total = 0
    for item in order:
        
        if "cafelatte" in item:
             total += 5000
        
        else:
             total += 4500
    return total