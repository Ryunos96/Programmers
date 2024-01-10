def solution(x, n):
    answer = []
    value = 0
    for i in range(0, n):
        answer.append(value + x)
        value += x
    return answer