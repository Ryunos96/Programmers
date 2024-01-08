def solution(slice, n):
    multiple = 1
    while True:
        if slice * multiple >= n:
            break
        multiple += 1
    return multiple