

def sequential_search(alist, item):
    """Sequential search
    Complexity:
    item is present: best case=1, worst case=n, avg=n/2
    item not present: best case=n, worst case=n, avg=n
    Args:
        alist (list): A list.
        item (int): The item to search.
    Returns:
        found (bool): Boolean with the answer of the search.
    Examples:
        >>> alist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        >>> sequential_search(alist, 3)
        False
        >>> sequential_search(alist, 13)
        True

    """
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


def ordered_sequential_search(ordered_list, item):
    """Ordered Sequential search
    Complexity:
    item is present: best case=1, worst case=n, avg=n/2
    item not present: best case=1, worst case=n, avg=n/2
    Args:
        ordered_list (list): An ordered list.
        item (int): The item to search.
    Returns:
        found (bool): Boolean with the answer of the search.
    Examples:
        >>> alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        >>> sequential_search(alist, 3)
        False
        >>> sequential_search(alist, 13)
        True

    """
    pos = 0
    found = False
    stop = False
    while pos < len(ordered_list) and not found and not stop:
        if ordered_list[pos] == item:
            found = True
        else:
            if ordered_list[pos] > item:
                stop = True
            else:
                pos += 1
    return found


def ordered_binary_search(ordered_list, item):
    """Binary search in an ordered list
    Complexity: O(log n)
    Args:
        ordered_list (list): An ordered list.
        item (int): The item to search.
    Returns:
        found (bool): Boolean with the answer of the search.
    Examples:
        >>> alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        >>> sequential_search(alist, 3)
        False
        >>> sequential_search(alist, 13)
        True

    """
    first = 0
    last = len(ordered_list)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if ordered_list[midpoint] == item:
            found = True
        else:
            if item < ordered_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

        return found
