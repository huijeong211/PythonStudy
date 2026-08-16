def solution(todo_list, finished):
    answer = []
    
    
    for i, is_done in enumerate(finished):
        if not is_done:
            answer.append(todo_list[i])
    return answer