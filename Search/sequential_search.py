# coding = 'utf-8'
def sequential_search(alist, item):
    '''
    顺序查找
    :param list: 被查找的list
    :param item: 需要查找的数字
    :return: 是否找到,和在第几个
    '''
    position = 0
    found = False
    while position < len(alist) and not found:
        if item == alist[position]:
            found = True
        else:
            position = position + 1
    return (found, position)


if __name__ == '__main__':
    test_list=[1,2,3,6,5,4,9,8,7]
    print(sequential_search(test_list,3))
    print(sequential_search(test_list,10))
    print('finish')
