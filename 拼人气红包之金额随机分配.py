import random


def allocate_money(total, num):
    # total-总金额，num-分配份数
    total = round(total, 2)
    num = int(num)
    if total <= 0 or num <= 0 or total > 200 or num > 200:
        return

    # 初始化列表，为每一个列表元素分配一个随机量，并计算随机量总和 
    result = []
    radnum_sum = 0
    for i in range(num):
        result.append(random.random())
        radnum_sum += result[i]

    # 总金额除以随机量总和，得到一个计算基数
    # 计算基数乘以每一个列表元素随机量，得到一份随机分配金额 
    total_base = total/radnum_sum
    for i in range(num):
        result[i] = round(total_base*result[i], 2)

    # 将累计误差加至某一列表元素，判断结果是否为零及负数，选择相加或下一个元素 
    check_sum = round(total-sum(result), 2)
    if check_sum != 0:
        for i in range(num):
            if (result[i]+check_sum) > 0:
                result[i] += check_sum
                break

    return result

if __name__ == "__main__":
    result = allocate_money(99, 9)
    for i in result:
        print(i)
    print('Sum:', sum(result))
    print('Err:', 99-sum(result), round(99-sum(result), 2))
