def solution(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []
    
    # 뒤에서부터 한 자리씩 가져와 더합니다.
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
            
        result.append(str(carry % 10))
        carry //= 10
        
    # 역순으로 저장된 결과를 다시 뒤집어 문자열로 합칩니다.
    return "".join(reversed(result))