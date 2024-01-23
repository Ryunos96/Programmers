def solution(numbers, n):
    sumnum = 0
    i = 0
    while True:
        if sumnum > n:
            return sumnum
        sumnum += numbers[i]
        i += 1
    return sumnum