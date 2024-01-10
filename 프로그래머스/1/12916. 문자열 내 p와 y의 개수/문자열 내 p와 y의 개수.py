def solution(s):
    answer = True
    s = s.lower()
    nump = 0
    numy = 0
    for idx in s:
        if idx == 'p':
            nump += 1
        elif idx == 'y':
            numy += 1
    if (nump == numy or (nump == 0 and numy == 0)):
        return True
    return False