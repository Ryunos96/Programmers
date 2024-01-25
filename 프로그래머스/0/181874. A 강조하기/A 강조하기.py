def solution(myString):
    string = list(myString)
    answer = ''
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'A':
            answer += string[i].upper()
        else:
            answer += string[i].lower()
    return answer