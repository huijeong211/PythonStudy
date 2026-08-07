def solution(code):
    ret = ''
    mode = 0
    
    for idx in range(len(code)):
        char = code[idx]
                     
        if mode == 0:
            if char == "1":
                     mode = 1 #모드 전환
                     
            else:
                if idx % 2 == 0:
                     ret += char
                     
        else:
            if char == "1":
                mode = 0
            else:
                if idx % 2 != 0:
                     ret += char
                     
    if ret == "":
        return "EMPTY"
    else:
        return ret