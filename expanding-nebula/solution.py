#!/usr/bin/env python2

PREV = (
    (
        ((0, 0), (0, 0)), ((0, 0), (1, 1)), ((0, 1), (0, 1)), ((0, 1), (1, 0)),
        ((0, 1), (1, 1)), ((1, 0), (0, 1)), ((1, 0), (1, 0)), ((1, 0), (1, 1)),
        ((1, 1), (0, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 0)), ((1, 1), (1, 1)),
    ),
    (
        ((1, 0), (0, 0)), ((0, 1), (0, 0)), ((0, 0), (1, 0)), ((0, 0), (0, 1)),
    ),
)

def next(m):
    """
    Takes matrix m 2x2 and returns next step for 0,0 cell based on neighbours.
    """
    return sum(m[0]+m[1]) == 1

def prev_states(row):
    """
    Returns all states produce given row
    """
    complements = ((0, 0), (0, 1), (1, 0), (1, 1))
    prev_row = PREV[row[0]]
    for i in range(1, len(row)):
        curr_row = []
        for state in prev_row:
            for complement in complements:
                # check if this combination produces current cell on next step
                if next((state[i], complement)) == row[i]:
                    curr_row.append(state + (complement,))
        prev_row = tuple(curr_row)
    return (tuple(zip(*i)) for i in prev_row)

def solution(g):
    """
    >>> solution([[True, False], [False, True]])
    12
    >>> solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
    11567
    >>> solution([[True, False, True], [False, True, False], [True, False, True]])
    4
    >>> solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
    254
    """
    prev_rows = prev_states(g[0])
    prev_count = {}
    for prev_row in prev_rows:
        prev_count[prev_row[0]] = 1

    for row in g:
        prev_rows = prev_states(row)
        count = {}
        for prev_row in prev_rows:
            if prev_row[0] not in prev_count:
                prev_count[prev_row[0]] = 0
            if prev_row[1] not in count:
                count[prev_row[1]] = 0
            count[prev_row[1]] += prev_count[prev_row[0]]
        prev_count = count

    return sum(prev_count.values())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
