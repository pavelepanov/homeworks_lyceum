def find_max_number():
    with open('t3.txt', 'r') as file:
        data = file.read()


    max_number = 0

    for i in range(len(data) - 11):
        if data[i:i+2] == 'KK' and data[i+4:i+6] == '43' and data[i+6:i+8].isdigit() and data[i+8:i+10] == '78' and data[i+10:i+13].isdigit() and data[i+13:i+15] == '34':
            number = int(data[i+4:i+6] + data[i+6:i+8] + data[i+10:i+13])
            max_number = max(max_number, number)

    return max_number

def product_of_odd_digits(number):
    product = 1
    for digit in str(number):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product

max_number = find_max_number()
result = product_of_odd_digits(max_number)

print(f"Произведение нечетных цифр: {result}")
