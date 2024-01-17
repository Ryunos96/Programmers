def solution(arr):
    if len(arr) == 1:
        arr[0] = -1
        return arr
    min_ = min(arr)
    arr.remove(min_)
    return arr