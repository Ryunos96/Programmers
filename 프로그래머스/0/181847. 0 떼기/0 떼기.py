def solution(n_str):
    temp = 0
    answer = ''
    for i in range(len(n_str)):
        if n_str[i] != '0':
            temp = i
            break
    for j in range(temp, len(n_str)):
        answer += n_str[j]
    return answer