def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer = answer + absolutes[i]
        else:
            answer = answer + ((absolutes[i]) * (-1))
    return answer