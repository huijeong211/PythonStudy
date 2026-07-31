def solution(my_string, queries):
    
    for s,e in queries:
        
        front = my_string[:s]
        middle = my_string[s : e+1][::-1]
        back = my_string[e+1:]
        
        my_string = front+middle+back
        
    return my_string
    