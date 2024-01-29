def solution(myString):
    answer = list(myString)
    temp = ''
    for i in answer:
        if i <= 'l':
            temp += 'l'
            continue
        temp += i
    return temp