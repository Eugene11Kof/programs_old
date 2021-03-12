import random
#карты
nominal = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 2,
    'Q' : 3,
    'K' : 4,
    'A' : 11
}
koloda = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] * 4
print(koloda)

#игра
my = [] #набор моих карт
my_points = []  #накопление моих очков
bot_points = [] #накопление очков крупье (бота)
game = 'play'
game_bot = 'play'
x = random.sample(koloda, 1)
my.append(x[0])
print('вам выпало', x[0])
print(my, 'это ваш набор карт на данный момент')
while game == 'play':
    choice = input('берете еще?')
    if choice == 'да':
        x = random.sample(koloda, 1)
        my.append(x[0])
        my_points.append(nominal.get(x[0]))
        print('вам выпало', x[0])
        print(my, 'это ваш набор карт на данный момент')
        if sum(my_points) > 21:
            game = 'stop'
    elif choice == 'нет':
        game = 'stop'
while game_bot == 'play':
    y = random.sample(koloda, 1)
    bot_points.append(nominal.get(y[0]))
    if sum(bot_points) > 15:
        game_bot = 'stop'

#подсчёт очков
if sum(my_points) > 21:
    print('вы проиграли')
    print('ваши очки:', sum(my),'очки крупье:', sum(bot))
elif sum(bot_points) > 21:
    print('вы выиграли'),
    print('ваши очки:', sum(my),'очки крупье:', sum(bot))
else:
    if sum(my_points) > sum(bot_points):
        print('вы выиграли'),
        print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))
    else:
        print('вы проиграли')
        print('ваши очки:', sum(my_points), 'очки крупье:', sum(bot_points))