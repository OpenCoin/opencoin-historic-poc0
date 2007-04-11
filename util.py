"""Utility functions"""
import pickle

def encodeKey(key):
    return pickle.dumps(key)

def decodeKey(string):
    return pickle.loads(string)

def partition(value, denominations):
    """
    Partition an integer into smaller summands from a given list 
    of allowed summands. Return list of summands and rest.

    >>> partition(45, [64,32,16,8,4,2,1])
    ([16, 8, 8, 4, 4, 2, 1, 1, 1], 0)
    >>> partition(45, [64,32,16,8])
    ([16, 8, 8, 8], 5)
    >>> partition(45, [64,32])
    ([32], 13)
    >>> partition(45, [64])
    ([], 45)
    """

    denominations.sort()
    smallest=denominations[0]

    part = []
    rest = value

    while rest > 0 :
	denominations = [i for i in denominations if i <= rest/2]
	if denominations == [] : break
        p = max (denominations)
	part.append(p)
	rest -= p

    while rest >= smallest :
	part.append(smallest)
	rest -= smallest

    return (part, rest)


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
