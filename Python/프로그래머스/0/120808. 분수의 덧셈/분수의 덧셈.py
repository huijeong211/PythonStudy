import math

def solution(numer1, denom1, numer2, denom2):
    
    #통분 공식
    numer = numer1*denom2 + numer2*denom1
    denom = denom1 *denom2
    
    #최대공약수 함수: gcd
    
    gcd_val = math.gcd(numer,denom)
    return [numer // gcd_val, denom // gcd_val]