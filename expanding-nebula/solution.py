#!/usr/bin/env python2

def solution(g):
    """
    >>> solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
    11567
    >>> solution([[True, False, True], [False, True, False], [True, False, True]])
    4
    >>> solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
    254
    """
    return 4


if __name__ == "__main__":
    import doctest
    doctest.testmod()
