def solution(a, b, c, d):
    dice = [a,b,c,d]
    dice.sort()
    
    a,b,c,d = dice[0], dice[1], dice[2], dice[3]
    
    if a == d:
        return 1111 * a
    elif a== c:
        return (10 * a + d)**2
    elif b == d:
        return (10*b + a)**2
    elif a == b and c == d:
        return (a + c) * abs(a - c)
    elif a == b:
        return c *d
    elif b == c:
        return a*d
    elif c== d:
        return a*b
    else:
        return a
        
    
    