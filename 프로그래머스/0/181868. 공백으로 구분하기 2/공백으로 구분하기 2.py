def solution(my_string):
    answer = []
    temp = ''
    for i in range(len(my_string)):
        if my_string[i] == ' ':
            if temp != '':
                answer.append(temp)
            temp = ''
            continue
        temp += my_string[i]
        if i == len(my_string) - 1:
            answer.append(temp)
    return answer