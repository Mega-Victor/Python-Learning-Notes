def bubble_sort(alist):
    '''
    冒泡排序,每次冒泡一遍最后一个是最大的数字,下一次只需要比较n-1次
    冒泡排序(bubble sort)：每个回合都从第一个元素开始和它后面的元素比较，
    如果比它后面的元素更大的话就交换，一直重复，直到这个元素到了它能到达的位置。
    每次遍历都将剩下的元素中最大的那个放到了序列的“最后”(除去了前面已经排好的那些元素)。
    注意检测是否已经完成了排序，如果已完成就可以退出了。时间复杂度$O(n^2)
    :param list: 需要排序的list
    :return:排序好的list
    '''
    numLen = len(alist) - 1
    for j in range(numLen):
        for i in range(numLen - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return list


if __name__ == '__main__':
    test_list = [1, 5, 6, 9, 8, 5, 4, 7, 3, 2, 25, 39, 99, 4, 8, 5]
    print(bubble_sort(test_list))
