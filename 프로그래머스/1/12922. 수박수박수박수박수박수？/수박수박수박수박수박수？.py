def solution(n):
    answer = []
    half = int(n / 2)
    i = 0
    if n % 2 == 1:
        answer.append('수')
        for i in range(0, half):
            answer.append('박수')
            i += 1
        answer_1 = ''.join(answer)
        return answer_1
    else :
        for i in range(0, half):
            answer.append('수박')
            i += 1
        answer_1 = ''.join(answer)
        return answer_1
    return answer