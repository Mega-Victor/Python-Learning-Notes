def insertion_sort(a_list):
    '''
    每次假设前面的元素都是已经排好序了的，然后将当前位置的元素插入到原来的序列中，
    为了尽快地查找合适的插入位置，可以使用二分查找。时间复杂度$O(n^2)$，
    别误以为二分查找可以降低它的复杂度，因为插入排序还需要移动元素的操作！
    :param list:
    :return:
    '''
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return a_list


if __name__ == '__main__':
    test_list = [0, 12, 28, 78, 13, 17, 19, 32, 42, 36,95,25,15 ]
    print(test_list)
    print(insertion_sort(test_list))

