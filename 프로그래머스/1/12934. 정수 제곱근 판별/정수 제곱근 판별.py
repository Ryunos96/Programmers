import math
def solution(n):
    if (math.floor(math.sqrt(n))*math.floor(math.sqrt(n))) == n:
        return ((math.floor(math.sqrt(n))+1) * (math.floor(math.sqrt(n))+1))
    return -1