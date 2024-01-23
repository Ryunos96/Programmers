def solution(num_list):
    leng = len(num_list)
    if num_list[leng-2] < num_list[leng-1]:
        num_list.append(num_list[leng-1] - num_list[leng-2])
    else:
        num_list.append(num_list[leng-1] * 2)
    return num_list