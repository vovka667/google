def solution(l, t):
    sum = 0
    begin = 0
    for end in range(len(l)):
        sum += l[end]
        while sum > t:
            sum -= l[begin]
            begin += 1
        if sum == t:
            return [begin, end]
    return [-1, -1]
