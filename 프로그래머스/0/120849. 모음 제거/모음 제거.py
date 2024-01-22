def solution(my_string):
    answer = ''
    length = len(my_string)
    for i in range(0, length):
        if my_string[i] != 'a' and my_string[i] != 'e' and my_string[i] != 'i' and my_string[i] != 'o' and my_string[i] != 'u':
            answer += my_string[i]
    return answer