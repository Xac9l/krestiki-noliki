def nachalo():
    while True:
        print('Вы хотите начать игру? (Y - Да, N - Нет)')
        otvet = input()
        if otvet == 'Y' or 'y':
            game()
        elif otvet == 'N' or 'n':
            print('Игры не будет.')
            break
        else:
            print('Вы ввели неверный ответ!')
            continue
def otobrajenie_karty(karta):
    c = 0
    for elem in karta:
        print(' | '.join(elem))
        c += 1
        if c < 3:
            print('-' * 9)
def proverka_pobeditel(karta):
    for i in range(3):
        if karta[0][i] == karta[1][i] == karta[2][i] != ' ' or karta[i][0] == karta[i][1] == karta[i][2] != ' ':
            return True
    if karta[0][0] == karta[1][1] == karta[2][2] != ' ' or karta[0][2] == karta[1][1] == karta[2][0] != ' ':
        return True
    return False
def proverka_zapolnenoy_karty(karta):
    for elem in karta:
        if ' ' in elem:
            return False
    return True
def game():
    karta = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    otobrajenie_karty(karta)
    while True:
        stroka = int(input(f'Игрок {player}, введите номер строки (1 - 3): ')) - 1
        stolb = int(input(f'Игрок {player}, введите номер столбца (1 - 3): ')) - 1
        if stroka < 0 or stroka > 2 or stolb < 0 or stolb > 2:
            print('Вы ввели неверные координаты!')
            continue
        if karta[stroka][stolb] == ' ':
            karta[stroka][stolb] = player
            otobrajenie_karty(karta)
        else:
            print('Данная клетка занята, введите другую координату')
            continue
        if proverka_pobeditel(karta):
            print(f'Игрок {player} победил!')
            break
        if proverka_zapolnenoy_karty(karta):
            print('Ничья!')
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
nachalo()
