"""Reverse list in place.

You cannot do this with reversed(), .reverse(), or list slice
assignment!

    >>> lst = []
    >>> rev_list_in_place(lst)
    >>> lst
    []

    >>> lst = ['a']
    >>> rev_list_in_place(lst)
    >>> lst
    ['a']

    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    >>> lst
    [3, 2, 1]

    >>> lst = [1, 2, 3, 4]
    >>> rev_list_in_place(lst)
    >>> lst
    [4, 3, 2, 1]
"""


def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    rev_lst = []
    # if lst is empty 
    # return an empty lst
    if lst == []:
        return None
    # the length of the lst is 1
    # return that lst
    if range(len(lst)) == 1:
        return lst
    # for the length of the lst
    # remove the last item of the lst
    # add it to the new_lst 
    # return the new_lst
    for item in range(len(lst)):
        rev_lst.append(lst.pop())

    return rev_lst
    # place it in the begining 
    # then move the next item and place it after the first

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n")
