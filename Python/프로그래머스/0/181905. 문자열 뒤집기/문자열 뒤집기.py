def solution(my_string, s, e):
   # 앞 자르고 뒤 자르고 중간 부분은 역순 취해서 리턴

    front = my_string[:s]
    
    middle = my_string[s:e+1][::-1]
    
    back = my_string[e+1:]
    
    return front+middle+back

#[:s] : 처음~ s직전까지 (앞부분)[s:] : s ~ 끝까지 (뒷부분)