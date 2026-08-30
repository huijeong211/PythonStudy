def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', " ").replace('c',' ')
    result = myStr.split()
    return result if result else ["EMPTY"]