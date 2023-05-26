while True:
    action = 1
    num = int(input('enter your number: '))
    while num != 1:
        num = num / 2 if num % 2 == 0 else 3 * num + 1
        print(f'Action {action}: {num}')
        action += 1