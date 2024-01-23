def solution(my_string):
    mystr = list(my_string)
    for i in range(len(my_string)):
        if mystr[i] >= 'a' and mystr[i] <= 'z':
            mystr[i] = mystr[i].upper()
        elif mystr[i] >= 'A' and mystr[i] <= 'Z':
            mystr[i] = mystr[i].lower()
    return ''.join(mystr)