def solution(n):
    st = sorted(list(str(n)), reverse=True)
    st1 = int(''.join(st))
    return st1