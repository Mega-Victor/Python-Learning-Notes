def merge_sort(a_list):
    '''
    典型的是二路合并排序，将原始数据集分成两部分(不一定能够均分)，分别对它们进行排序，
    然后将排序后的子数据集进行合并，这是典型的分治法策略。时间复杂度O(nlogn)
    :param a_list:
    :return:
    '''
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0;j=0;k=0;
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j=j+1
            k=k+1
    print("Merging ", a_list)

unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]

print(merge_sort(unsortedArray))