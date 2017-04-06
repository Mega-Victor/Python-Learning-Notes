def selection_sort(alist):
    '''
    每个回合都选择出剩下的元素中最小的那个，选择的方法是首先默认第一元素是最小的，
    如果后面的元素比它小的话，那就更新剩下的最小的元素值，找到剩下元素中最小的之后将它放入到合适的位置就行了。
    和冒泡排序类似，只是找剩下的元素中最小的方式不同而已。时间复杂度$O(n^2)$
    :param list:
    :return:
    '''
    for i in range(len(alist)):
        min_index = i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
                alist[min_index],alist[i] = alist[i],alist[min_index]
    return alist


if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, 36,95,25,15 ]
    print(selection_sort(test_list))