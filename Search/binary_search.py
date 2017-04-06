def binary_search(alist,item):
    '''
    二分查找
    :param list:
    :param item:
    :return:
    '''
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found =True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return (found,midpoint)


if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, 36,95,25,15 ]
    print(binary_search(test_list, 2))
    print(binary_search(test_list, 13))
    print(binary_search(test_list, 98))
