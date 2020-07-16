def solution(xs):
    min_negative = 0
    nonzeros = 0
    result = long(0)

    for value in xs:
        if value == 0:
            continue
        nonzeros += 1
        if result == 0:
            result = long(1)
        result *= long(value)

        if value < 0:
            if min_negative < value or min_negative == 0:
                min_negative = value

    if result < 0:
        if nonzeros == 1:
            if len(xs) == 1:
                return(result)
            else:
                return str(0)
        else:
            result /= long(min_negative)

    return str(result)
