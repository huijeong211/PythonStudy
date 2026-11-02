def solution(n):
    answer = []
    d = 2
    
    # d를 2부터 시작하여 n을 나눌 수 있을 때까지 나눕니다.
    while d <= n:
        if n % d == 0:
            # 아직 리스트에 없는 소인수라면 추가합니다.
            if d not in answer:
                answer.append(d)
            n //= d
        else:
            d += 1
            
    return answer