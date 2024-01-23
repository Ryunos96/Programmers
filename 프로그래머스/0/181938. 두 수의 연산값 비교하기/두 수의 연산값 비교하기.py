def solution(a, b):
    int_int = a * b * 2
    int_str = int(str(a) + str(b))
    if int_int <= int_str:
        return int_str
    return int_int