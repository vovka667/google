from collections import deque


def find_path(sources, sinks, flow):
    """
    >>> find_path([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
    [0, 1, 2, 3]
    >>> find_path([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    [0, 2, 4]
    """
    def walk(source, sinks, visited, path):
        visited[source] = True
        for child, capacity in enumerate(flow[source]):
            if visited[child] or capacity == 0:
                continue
            if child in sinks:
                return path + [child]
            found_path = walk(child, sinks, visited, path + [child])
            if len(found_path) > 0:
                return found_path
        return []

    visited = [False] * len(flow)

    for source in sources:
        found_path = walk(source, sinks, visited, [source])
        if len(found_path) > 0:
            return found_path
    return []


def solution(entrances, exits, path):
    print "flow: %s" % path
    print "path: %s" % find_path(entrances, exits, path)
    return 6


if __name__ == "__main__":
    import doctest
    doctest.testmod()
