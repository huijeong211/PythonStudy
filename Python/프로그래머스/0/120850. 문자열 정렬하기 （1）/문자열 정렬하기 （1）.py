def solution(my_string):
    # 1. 문자열의 각 문자가 숫자("0"~"9")인지 확인하고 숫자인 것만 정수형으로 변환해 리스트에 담습니다.
    numbers = [int(char) for char in my_string if char.isdigit()]
    
    # 2. 오름차순으로 정렬하여 반환합니다.
    return sorted(numbers)