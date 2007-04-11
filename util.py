"""Utility functions"""
import pickle

def encodeKey(key):
    return pickle.dumps(key)

def decodeKey(string):
    return pickle.loads(string)

def partition(value, denominations):
    """
    Partition an integer into smaller summands from a given 
    list of possible summands. Return list of summands 
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
