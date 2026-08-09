def solution(n, k):
    # k부터 시작해서 n까지 k씩 건너뛰며 리스트로 만든다
    return list(range(k, n + 1, k))