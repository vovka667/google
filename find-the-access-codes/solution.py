from collections import defaultdict

def solution(l):
    result = 0
    cache = defaultdict(int)

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] != 0:
                continue

            if cache[j] != 0:
                result += cache[j]
                continue

            for k in range(j+1, len(l)):
                if l[k] % l[j] != 0:
                    continue

                result += 1
                cache[j] += 1

    return result
