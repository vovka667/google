def solution(l):
    result = 0

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] != 0:
                continue

            for k in range(j+1, len(l)):
                if l[k] % l[j] != 0:
                    continue

                result += 1

    return result
