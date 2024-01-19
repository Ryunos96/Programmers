def solution(my_string, n):
    answer = ''
    for i in range(0, len(my_string)):
        for j in range(1, n+1):
            answer += my_string[i]
    return answer