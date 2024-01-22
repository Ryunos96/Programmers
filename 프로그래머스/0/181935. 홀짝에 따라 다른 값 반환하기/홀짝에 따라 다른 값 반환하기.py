def solution(n):
    sum_num = 0
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            sum_num += i
    elif n % 2 == 0:
        for i in range(2, n+1, 2):
            sum_num += i**2
    return sum_num