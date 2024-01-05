def solution(numbers):
    sum = 0
    len = 0
    avg = 0
    for i in numbers:
        sum = sum + i
        len += 1
    avg = sum / len
    return avg