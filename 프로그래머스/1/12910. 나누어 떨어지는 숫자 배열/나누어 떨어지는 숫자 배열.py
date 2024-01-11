def solution(arr, divisor):
    answer = []
    flag = 0
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            flag = 1
    if flag == 1:
        answer.sort()
        return answer
    elif flag == 0:
        return [-1]