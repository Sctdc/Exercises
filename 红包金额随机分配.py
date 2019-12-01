import random


def allocate_money(total, num):
    total = round(total, 2)
    num = int(num)
    if total <= 0 or num <= 0 or total > 200 or num > 200:
        return

    result = [random.random() for no in range(num)]
    total_base = total/sum(result)
    for no in range(num):
        result[no] = round(total_base*result[no], 2)

    check_sum = total-sum(result)
    if check_sum != 0:
        for no in range(num):
            if (result[no]+check_sum) > 0:
                result[no] = round(result[no]+check_sum, 2)
                break

    return result


if __name__ == "__main__":
    total = 18
    num = 6
    result = allocate_money(total, num)
    if result is not None:
        for item in result:
            print(item)
        print('Sum:', sum(result))
        print('Err:', total-sum(result), round(total-sum(result), 2))
    else:
        print('List is None.')
