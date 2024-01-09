def solution(n, k):
    answer = n * 12000 + k * 2000
    while n >= 10:
        answer = answer - 2000
        n -= 10
    return answer