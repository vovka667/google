from collections import deque


def find_path(sources, sinks, network):
    """
    >>> find_path([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
    [0, 1, 2, 3]
    >>> find_path([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    [0, 2, 4]
    """
    def walk(source, sinks, visited, path):
        visited[source] = True
        for child, capacity in enumerate(network[source]):
            if visited[child] or capacity == 0:
                continue
            if child in sinks:
                return path + [child]
            found_path = walk(child, sinks, visited, path + [child])
            if len(found_path) > 0:
                return found_path
        return []

    visited = [False] * len(network)

    for source in sources:
        found_path = walk(source, sinks, visited, [source])
        if len(found_path) > 0:
            return found_path
    return []


def solution(entrances, exits, path):
    """
    >>> solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
    6
    >>> solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    16
    """

    flows = [[0 for _ in node] for node in path]
    network = path[:]
    flow = 0
    while True:
        augmenting_path = find_path(entrances, exits, network)
        if len(augmenting_path) == 0:
            break
        augment = min([network[augmenting_path[i]][augmenting_path[i+1]] for i in range(len(augmenting_path)-1)])
        for i in range(len(augmenting_path)-1):
            src = augmenting_path[i]
            dst = augmenting_path[i+1]
            network[src][dst] -= augment
            network[dst][src] += augment
        flow += augment

    return flow


if __name__ == "__main__":
    import doctest
    doctest.testmod()
