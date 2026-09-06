def solution(arr, delete_list):
    delete_set = set(delete_list)
    
    return [num for num in arr if num not in delete_list]