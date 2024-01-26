def solution(box, n):
    width = int(box[0] / n)
    length = int(box[1] / n)
    height = int(box[2] / n)
    return width * length * height