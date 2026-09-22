def solution(money):
    cups = money //5500
    
    charge = money % 5500
    
    return [cups, charge]