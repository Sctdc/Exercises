import random


def allocate_money(total, num):
    # 初始化总金额(total，保留2位小数），分配份数（num，取整）
    total = round(total, 2)
    num = int(num)
    if total <= 0 or num <= 0 or total > 200 or num > 200:
        return

    # 初始化列表，为每一个列表元素分配一个随机量
    # 总金额除以列表元素随机量总和，得到计算基数
    # 计算基数乘以每一个列表元素随机量，得到一份随机分配金额 
    result = [random.random() for no in range(num)]
    total_base = total/sum(result)
    for no in range(num):
        result[no] = round(total_base*result[no], 2)

    # 将累计误差加至某一列表元素，若结果大于零，退出，否则选择下一列表元素
    check_sum = round(total-sum(result), 2)
    if check_sum != 0:
        for no in range(num):
            if (result[no]+check_sum) > 0:
                result[no] += check_sum
                break

    return result

if __name__ == "__main__":
    result = allocate_money(99, 9)
    for item in result:
        print(item)
    # 验证总金额 
    print('Sum:', sum(result))
    print('Err:', 99-sum(result), round(99-sum(result), 2))
