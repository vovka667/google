"""
>>> solution([1, 1])
2
>>> solution([1, 7, 3, 21, 13, 19])
0
"""

from fractions import gcd

def solution(banana_list):
	guards = {}
	for i, bananas_i in enumerate(banana_list):
		guards[i] = Guard()
		for j, bananas_j in enumerate(banana_list):
			if i == j:
				continue
			if infinite(bananas_i, bananas_j):
				guards[i].loops[j] = 1

	guardIDs = guards.keys()
	#print guards

	result = 0
	while len(guardIDs) > 0:
		guardIDs.sort(key=lambda x: len(guards[x].loops.keys()), reverse=True)
		#print("\n\t".join('%s' % guards[id] for id in guardIDs))
		curID = guardIDs.pop()
		curGuard = guards[curID]
		loops = curGuard.loops.keys()
		if len(loops) == 0:
			result += 1
			continue
		for id in loops:
			del guards[id].loops[curID]

		loops.sort(key=lambda x: len(guards[x].loops.keys()), reverse=True)
		pairID = loops.pop()
		pairGuard = guards[pairID]

		#print "\t", pairGuard.loops.keys()
		for id in pairGuard.loops.keys():
			#print "\tDelete %d from %d" % (pairID, id)
			#print "\t", guards
			#print "\t", guards[id].loops.keys()
			del guards[id].loops[pairID]

		guardIDs.remove(pairID)

	return result

def infinite(x, y):
    factor = (x+y)/gcd(x,y)
    return bool(factor & (factor - 1))

class Guard:
    def __init__(self):
        self.loops = {}
    def __str__(self):
        return "loops: %s" % (self.loops.keys())
    def __repr__(self):
	return self.__str__()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
