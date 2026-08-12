def solution(arr, intervals):
    [a1,b1], [a2,b2] =intervals
    
    return arr[a1 : b1 +1] + arr[a2 : b2+1]
#b1, b2 인덱스까지 포함하기 위해 +1