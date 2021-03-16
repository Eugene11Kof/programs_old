import random
from time import sleep

# карты
nominal = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 2,
    'Q': 3,
    'K': 4,
    'A': 11
}
mKoloda = [
    '2','3','4','5',
    '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
koloda = []
for m in ["♥", "♦", "♣", "♠"]:
    for i in mKoloda:
        koloda.append(i + m)

card = None

def A(i, iPoints):
    for x in range(0, len(i)):
        if i[x][0] == "A" and iPoints[x] == 11:
            iPoints[x] = 1
    return iPoints

# игра
money = 500 #кол-во денег на руках
more = 'да' #продолжение игры
print('Добро пожаловать в игру. У вас 500$ на руках.')
while money > 0 and money < 1000 and more != 'нет':
    print('Сколько будете ставить?')
    stavka = int(input())
    if stavka >= 10 and stavka <=money and stavka <= (1000-money):
        print('ставка принята')
    #######
    my = []  # набор моих карт
    my_points = []  # накопление моих очков
    bot = []
    bot_points = []  # накопление очков крупье (бота)
    game = True  # одна игра
    random.shuffle(koloda)
    card = koloda.pop()
    my.append(card)
    my_points.append(nominal.get(card[0]))
    print('вам выпало', card)
    print(my, 'это ваш набор карт на данный момент. Очков:' + str(sum(my_points)))
    while game:
        choice = input('берете еще?')
        if choice == 'да':
            random.shuffle(koloda)
            card = koloda.pop()
            my.append(card)
            my_points.append(nominal.get(card[0]))
            print('вам выпало', card)
            if sum(my_points) > 21:
                my_points = A(my, my_points)
            print(my, 'это ваш набор карт на данный момент. Очков:' + str(sum(my_points)))
            if sum(my_points) > 21:
                print('у вас перебор')
                game = False
        elif choice == 'нет':
            game = False
    game = True
    while game:
        print("Крупье берет карту...")
        sleep(random.randint(100, 500) / 100)
        random.shuffle(koloda)
        card = koloda.pop()
        bot.append(card)
        bot_points.append(nominal.get(card[0]))
        if sum(bot_points) > 21:
            bot_points = A(bot, bot_points)
        print("Крупье выпало ", card)
        print("Его карты: ", bot, ". Очков: ", sum(bot_points))
        sleep(random.randint(10, 300) / 100)
        if sum(bot_points) > 15:
            game = False
    print("---------------")
    # подсчёт очков
    result = '0'
    print("Ваши карты: ", my)
    print("Карты крупье: ", bot)
    sleep(random.randint(10, 300) / 100)
    if sum(my_points) > 21:
        if sum(bot_points) <= 21:
            print('вы проиграли')
            result = 'lose'
        elif sum(bot_points) > 21:
            print('ничья, так как и Вы и крупье перебрали очки')
            result = 'draw'
        print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))
    elif sum(bot_points) > 21:
        print('вы выиграли')
        result = 'win'
        print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))
    else:
        if sum(my_points) > sum(bot_points):
            print('вы выиграли')
            result = 'win'
            print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))
        else:
            print('вы проиграли')
            result = 'lose'
            print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))
    sleep(random.randint(10, 300) / 100)
    #подсчёт денег
    if result == 'win':
        money += stavka
        print('вы выиграли',stavka,'$')
    elif result == 'lose':
        money -= stavka
        print('вы проиграли', stavka, '$')
    print('У вас', money, '$ на руках.')
    sleep(random.randint(10, 300) / 100)
    more = input('Хотите продолжить игру?')
sleep(random.randint(10, 700) / 100)
#финальный результат:
if money == 0:
    print('Вы проиграли все деньги. Игра на сегодня закончена.До скорой встречи!')
if money == 1000:
    print('У вашего соперника закончились деньги. Ваш совокупный выигрыш составил 500$. До скорой встречи!')
