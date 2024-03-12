categories = {
    'молоко': [45, 312, 54],
    'хлеб': [312, 32],
    'сыр': [3123, 312, 32]
}

print(list(categories.items()))

sred = 3123

for key, value in categories.items():
    if sred in value:
        print(key)
