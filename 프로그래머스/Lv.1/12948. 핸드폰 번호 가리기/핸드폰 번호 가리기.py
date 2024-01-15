def solution(phone_number):
    answer = list(phone_number)
    for i in range(0, len(phone_number) - 4):
        answer[i] = "*"
    answers = ''.join(answer)
    return answers