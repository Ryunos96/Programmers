def solution(n):
    x = 2;
    while x <= 1000000:
        if n % x == 1:
            break;
        x += 1
    return x