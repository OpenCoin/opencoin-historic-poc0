"""Utility functions"""


def partition(value, denominations):
    denominations.sort()
    smallest=denominations[0]

    part = []
    rest = value

    while rest > 0 :
	denominations = [i for i in denominations if i <= rest/2]
        n = 

