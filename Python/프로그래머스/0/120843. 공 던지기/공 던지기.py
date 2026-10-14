def solution(numbers, k):
    target_idx = (2 * (k-1)) % len(numbers)
    return numbers[target_idx]