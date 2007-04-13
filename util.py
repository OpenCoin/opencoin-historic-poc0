"""Utility functions"""
import pickle

def encodeKey(key):
    return pickle.dumps(key)

def decodeKey(string):
    return pickle.loads(string)


def encodeCoin(coin):
    return pickle.dumps(coin).encode('base64')
    
def decodeCoin(string):
    return pickle.loads(string.decode('base64'))


#Testing class for register Callback
class Testclass:

    def __init__(self):
        self.callbacks = {}

    def foo(self):
        print 'foo'
        for cb in getCallbacks(self,'foo'):
            cb()

#Simple standalone function
def bar():
    print 'bar'

def test_callbacks():
    """
    >>> t = Testclass()
    >>> registerCallback(t,'foo',bar)
    >>> t.foo()
    foo
    bar
    """


def registerCallback(obj,event,callback):
        getCallbacks(obj,event).append(callback)

def getCallbacks(obj,event):
    if hasattr(obj,'callbacks'):
        return obj.callbacks.setdefault(event,[])

        #obj.callbacks[event].append(callback)


def partition(denominations,value):
    """
    Partition an integer into smaller summands from a given list 
    of allowed summands. Return list of summands and rest.

    >>> partition([64,32,16,8,4,2,1],45)
    ([16, 8, 8, 4, 4, 2, 1, 1, 1], 0)
    >>> partition([64,32,16,8],45)
    ([16, 8, 8, 8], 5)
    >>> partition([64,32],45)
    ([32], 13)
    >>> partition([64],45)
    ([], 45)
    >>> partition([],45)
    ([], 45)

    """
    if not denominations:
        return ([],value)

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


def select_values(value_list, sum)
    rest = sum
    # delete all coins greater than sum
    value_list = [v for v in value_list if v <= sum]
    while not value_list = []
        max_value = 
        

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
