def solution(numbers):
    numbers.sort()
    max_idx = len(numbers)-1
    return numbers[max_idx] * numbers[max_idx - 1]