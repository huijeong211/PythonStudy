def solution(arr, flag):
    X = []
    
    for var,f in zip(arr,flag):
        if f:
            X.extend([var] * (var *2))
        else:
            X = X[:-var]
    
    return X