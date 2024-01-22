def solution(my_string, letter):
    answer = ''
    length = len(my_string)
    for i in range(0, len(my_string)):
        if my_string[i] != letter:
            answer += my_string[i]
    return answer