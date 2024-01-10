def solution(x):
    st = sum(list(map(int, str(x))))
    if x % st == 0:
        return True
    return False