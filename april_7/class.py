def multy(number):
    return number * 3


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def hello(name):
    return f'Hello, {name}!'


def hello_2(name, language):
    if language == 'русский':
        return f"Привет, {name}!"
    else:
        return f"Hello, {name}!"


def hello_3(n: int):
    print('Hello' * n)


def div(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count


def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


def series(n):
    summa = 0
    for i in range(1, n):
        summa += i * (i+1)
    return summa


def telephone(number):
    if number.startswith('+7') and (len(number)-2) == 10 and number[2:].isdigit():
        print(True)
    else:
        print(False)


def count_without_8(a):
    count = 0
    for _ in a:
        if '8' in str(_):
            pass
        else:
            count += 1
    return count


def final_price(price, discount=1):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    if final_price < 0:
        final_price = 0
    return final_price


def min_max(a, f='min'):
    if f == 'max':
        b = max(a)
    if f == 'min':
        b = min(a)

    count = a.count(b)
    return count


def my_list(n, value = 0):
    a = [value] * n
    return a


def num_correct(*n):
    total = list()
    for i in n:
        if 2 < i < 10:
            total.append(i)
    return total


def all_sort(*args):
    sorted_list = sorted(args)
    return sorted_list


def month(number, language='русский'):
    months_ru = {
        1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель",
        5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
        9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"
    }
    months_en = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    if language == 'русский':
        return months_ru.get(number)
    else:
        return months_en.get(number)


def final_price2(price, discount=1):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    if final_price < 0:
        final_price = 0
    return float(round(final_price, 2))


def final_price_3(*prices, discount=1):
    result = []
    for i in prices:
        result.append(final_price(i, discount))

    return result


def my_sum(*args):
    result = [0]
    total = 0

    for num in args:
        total += num
        result.append(total)

    return result
