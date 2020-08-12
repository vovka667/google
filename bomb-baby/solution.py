def solution(m, f):
    generations = long(0)
    m = long(m)
    f = long(f)
    while True:
        if m == 0 or f == 0:
            return 'impossible'

        if m == 1:
            generations += f - m
            break
        elif f == 1:
            generations += m - f
            break

        if m > f:
            generations += m // f
            m %= f
        elif f > m:
            generations += f // m
            f %= m

    return str(generations)
