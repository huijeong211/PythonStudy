def solution(my_string, indices):
    answer = ''
    
    for i, ch in enumerate(my_string):
        #enunarate: 순서가 있는 자료형(리스트, 문자열, 튜플 등)을 다룰 때 "몇 번째 항목인지(인덱스)"와 "그 항목의 값"을 동시에(쌍으로) 묶어서 하나씩 꺼내주는 역할
        if i not in indices:
            answer += ch
        
    return answer