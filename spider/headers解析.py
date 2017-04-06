headers = input("粘贴headers信息:\n")

def headers_format(h):
    '''
    函数用于转译网页headers信息
    :param h: 输入的headers原数据
    :return: 
    '''
    lst = h.split('\n')
    m=[]
    for i in lst:
        key = i.split(':')[0]
        value = i.split(':')[1]
        m.append([str(key),str(value)])
    return (dict(m))
print(headers_format(headers))