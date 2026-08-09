def solution(my_string):
    answer = [0] * 52
    
    for ch in my_string:
        if ch.isupper():
            #ch.isupper(): 문자가 대문자인지 확인하는 메서드
            idx = ord(ch) - ord('A')
            #ord(ch): 문자를 아스키코드 정수로 바꿔줌
            answer[idx] += 1
            
        else:
            idx = ord(ch) - ord('a') + 26
            answer[idx] += 1

    return answer