def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    min_negative = 0
    nonzeros = 0
    result = 0

    for value in xs:
        if value == 0:
            continue
        nonzeros += 1
        if result == 0:
            result = 1
        result *= value

        if value < 0:
            if min_negative < value or min_negative == 0:
                min_negative = value

    if result < 0:
        if nonzeros == 1:
            result = 0
        else:
            result /= min_negative

    return str(result)
