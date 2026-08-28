def solution(myString, pat):
    s =""
    
    for x in myString:
        if x == "A":
            s += "B"
            
        else:
            s+= "A"
            
    return int (pat in s)