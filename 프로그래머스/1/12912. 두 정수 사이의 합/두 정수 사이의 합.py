def solution(a, b):
    if a >= b:
        max = a
        min = b
    else:
        max = b
        min = a
    answer = 0
    while max >= min:
        answer = min + answer
        min += 1
    return answer