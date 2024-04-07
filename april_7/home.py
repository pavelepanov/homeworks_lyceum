def nums(n):
   return [n-1, n+1]


def final_price(price, discount):
   disc = price * discount / 100
   final_price = price - disc
   if final_price < 0:
       final_price = 0
   return round(final_price, 2)


def my_abs(n: int):
    return abs(n)


def length(x):
    ans = str(abs(x))
    return len(ans)


def str_lower(name):
    words = name.split()
    ans = [word.lower() for word in words]
    return ans


def exchange(list1, list2):
    temp = list1.copy()
    list1.clear()
    list1.extend(list2)
    list2.clear()
    list2.extend(temp)


def assess_collapse(mass, astral_body='Earth'):
    CRITICAL = 1000
    GRAVITY = {"Earth": 9.8,
               "Jupiter": 24.79,
               "Moon": 1.63, }
    total_wight = mass * GRAVITY[astral_body]
    if CRITICAL > total_wight:
        return False
    else:
        return True


def calc_tiles(size, form=(165, 255)):
    return int(form[0]/size[0])*int(form[1]/size[1])


def average(*args):
    total = sum(args)
    show = total / len(args)
    return round(show, 2)


def same(*args):
    if args.count(args[0]) == len(args):
        return True
    else:
        return False


def count_list(*args):
    counts = [0] * 6
    for num in args:
        if 5 <= num <= 10:
            counts[num - 5] += 1

    return counts


def rectangle(n=2, m=2, s='*'):
    total = n * s
    for i in range(m):
        print(total)

