def solution(s):
    stack = []
    
    # 1. 공백을 기준으로 문자열을 쪼갭니다.
    for item in s.split():
        # 2. "Z"가 나오면 가장 최근에 더했던(스택에 들어간) 숫자를 빼냅니다.
        if item == "Z":
            if stack:
                stack.pop()
        # 3. 숫자인 경우 정수로 변환하여 스택에 담습니다.
        else:
            stack.append(int(item))
            
    # 4. 스택에 남아 있는 숫자들의 총합을 반환합니다.
    return sum(stack)