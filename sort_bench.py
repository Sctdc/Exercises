import random, datetime, copy


# 测试样本
def fill_list(n):
    x = [] 
    
    for i in range(n):
        x.append(round(random.random()*100, 2))

    return x


# 冒泡排序
def bubble_sort(x):
    end = len(x)

    for i in range(0, end-1):
        for j in range(i+1, end):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]


# 快速排序
# 普通写法
def quick_sort_1(x, left, right):
    if left >= right:
        return

    i = left
    j = right
    key = x[left]
    
    while i < j:
        while i < j and key <= x[j]:
            j = j -1
        x[i] = x[j]

        while i < j and key >= x[i]:
            i = i + 1
        x[j] = x[i]
    
    x[i] = key
    quick_sort_1(x, left, i-1)
    quick_sort_1(x, i+1, right)

# Pythonic写法
def quick_sort_2(x):
    if len(x) < 2:
        return x
    else:
        key = x[0]
        less, equal, greater = [], [key], []
        for m in x[1:]:
            if m < key:
                less.append(m)         
            elif m > key:
                greater.append(m)    
            else:
                equal.append(m)
        return quick_sort_2(less) + equal + quick_sort_2(greater)


list_1 = fill_list(5000)
list_2 = copy.deepcopy(list_1)
list_3 = copy.deepcopy(list_1)

print('冒泡排序:')
start = datetime.datetime.now()
bubble_sort(list_1)
end = datetime.datetime.now()
print(end-start)

print('快速排序_1:')
start = datetime.datetime.now()
quick_sort_1(list_2, 0, len(list_2)-1)
end = datetime.datetime.now()
print(end-start)

print('快速排序_2:')
start = datetime.datetime.now()
result = quick_sort_2(list_3)
end = datetime.datetime.now()
print(end-start)
