def solution(age):
    alphabet = 'abcdefghij'
    
    answer = ""
    
    for char in str(age):
        answer += alphabet[int(char)]
    return answer