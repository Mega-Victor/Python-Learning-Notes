## List ##
list是一种有序的集合，可以随时添加和删除其中的元素。

    - classmates = ['Michael', 'Bob', 'Tracy']
    - len(classmates)
    - classmates[0]
    - classmates[-1] 最后的元素
    - classmates.append('Adam')
    - classmates.insert(1, 'Jack')  classmates[1] = 'Sarah'
    - classmates.pop() 删除list末尾元素
    - classmates.pop(1)
    - s = ['python', 'java', ['asp', 'php'], 'scheme']list元素也可以是另一个list

## Tuple ##

tuple和list非常类似，但是tuple一旦初始化就不能修改。没有append()，insert()这样的方法。其他获取元素的方法和list是一样的

    
    - 如果要定义一个空的tuple，可以写成()。 t = (1, 2)
    - 只有1个元素的tuple定义时必须加一个逗号,t = (1,)

##dict##

dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

    - d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    - d['Adam'] = 67  把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
    - d.pop('Bob')
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

    >>> 'Thomas' in d
    False
二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
    >>> d.get('Thomas')
    >>> d.get('Thomas', -1)
    -1

##set##
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
    
     - s = set([1, 2, 3])    s = set([1, 1, 2, 2, 3, 3])  重复元素在set中自动被过滤
     - s.add(4)
     - s.remove(4)

## 条件判断 ##

    age = 3
    if age >= 18:
    print('adult')
    elif age >= 6:
    print('teenager')
    else:
    print('kid')

## input ##

    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
    print('00前')
    else:
    print('00后')
## 循环 ##

1.for……in
    
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
    print(name)
    
    sum = 0
    for x in range(101): //0-100
    sum = sum + x
    print(sum)


2.while

    sum = 0
    n = 99
    while n > 0:
    sum = sum + n
    n = n - 2
    print(sum)