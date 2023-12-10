def exchange(mystr: str) -> str:
    new_str = ''
    for i in mystr:
        if i == 'Ё':
            new_str += 'ё'
        elif i == 'ё':
            new_str += 'е'
        else:
            new_str += i

    return new_str


def sum_range(start, end):
    if start < end:
        return sum([i for i in range(start, end)])
    else:
        return sum([i for i in range(end, start)])


def merge_lists(l1, l2):
    return l1 + l2


def all_sort(*args):
    array = list(args)
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


def is_palindrome(mystr):
    if mystr == mystr[::-1]:
        return True
    else:
        return False


def sort_words_by_length(text):
    words = text.split()
    word_lengths = list(map(len, words))
    sorted_word_lengths, sorted_words = zip(*sorted(zip(word_lengths, words)))
    return sorted_words


def how_many_times(text):
    text = text.lower()
    count_p = text.count('p')
    count_y = text.count('y')
    count_t = text.count('t')
    count_h = text.count('h')
    count_o = text.count('o')
    count_n = text.count('n')

    return min(count_p, count_y, count_t, count_h, count_o, count_n)


def t9(words, digits):
    keypad = [" ", ".,-", "абвг", "дежз", "ийкл", "мноп", "рсту", "фхцч", "шщъы", "ьэюя"]
    digit_to_letter = {}
    for i in range(len(keypad)):
        for letter in keypad[i]:
            digit_to_letter[letter] = str(i)

    filtered_words = []
    for word in words.split():
        word_digits = ''.join([digit_to_letter.get(letter.lower(), '') for letter in word])
        if word_digits.startswith(digits):
            filtered_words.append(word)

    return ' '.join(filtered_words)
