def h_index(citations):
    """A scholar with an index of h, has published h papers
    each of which has been cited in other papers at least h times
    https://en.wikipedia.org/wiki/H-index

    Each iteration takes O(n).
    Time complexity is O(n**2)
    >>> h_index([1, 4, 1, 4, 2, 1, 3, 5, 6])
    4
    >>> h_index([10, 8, 5, 4, 3])
    4
    >>> h_index([2, 2])
    2
    >>> h_index([1, 1])
    1
    >>> h_index([1])
    1
    >>> h_index([5])
    0
    >>> h_index([])
    0
    """

    dct = {}
    for i in citations:
        dct[i] = len([x for x in citations if x >= i])

    l = [k for k, v in dct.items() if k == v]
    h = l[0] if l else 0

    return h
