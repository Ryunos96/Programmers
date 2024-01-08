def solution(array):
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                tmp = array [i]
                array[i] = array[j]
                array[j] = tmp
    answer = array[int(len(array)/2)]
    return answer