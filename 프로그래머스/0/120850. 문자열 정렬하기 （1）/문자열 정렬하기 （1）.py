def solution(my_string):
    answer = []
    temp = list(my_string)
    for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        for j in range(len(temp)):
            if i == temp[j]:
                answer.append(int(i))
    temp = answer.sort()
    return answer