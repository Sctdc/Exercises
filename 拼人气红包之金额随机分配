import random


def allocate_money(total, num):
    total = round(total, 2)
    num = int(num)
    if total <= 0 or num <= 0 or total > 200 or num > 200:
        return

    result = []
    radnum_sum = 0
    for i in range(num):
        result.append(random.random())
        radnum_sum += result[i]

    total_base = total/radnum_sum
    for i in range(num):
        result[i] = round(total_base*result[i], 2)

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
