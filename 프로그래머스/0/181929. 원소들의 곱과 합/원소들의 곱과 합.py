def solution(num_list):
    mul = 1
    sum_ = 0
    for i in range(len(num_list)):
        mul *= num_list[i]
        sum_ += num_list[i]
    if mul < sum_**2:
        return 1
    return 0