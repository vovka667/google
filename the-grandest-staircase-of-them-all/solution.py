from collections import defaultdict

cache = defaultdict(int)

# maximum amount of bricks could be attached to current height
def capacity(n):
    return (n * (n-1)) / 2

def staircase(height, bricks):
    if bricks > capacity(height):
        return 0
    if bricks < 3 or bricks == capacity(height):
        return 1

    next_max = min([bricks, height-1])
    key = '{},{}'.format(next_max, bricks)
    if cache[key] == 0:
        for i in range(next_max, 0, -1):
            cache[key] += staircase(i, bricks-i)

    return cache[key]

def solution(n):
    result = 0
    # TODO: replce 1 with max possible value
    for i in range(n):
        result += staircase(i, n-i)

    return result
