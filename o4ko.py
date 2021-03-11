import random
#колода
koloda = []
for i in range(2, 12):
    if i in [2,3,4]:
        for j in range(8):
            koloda.append(i)
    else:
        for j in range(4):
            koloda.append(i)
#игра
my = [] #накопление моих очков
bot = [] #накопление очков крупье (бота)
game = 'play'
x = random.sample(koloda, 1)
print(x[0])
my.append(x[0])
y = random.sample(koloda, 1)
bot.append(y[0])
while game == 'play':
    choice = input('берете еще?')
    if choice == 'да':
        x = random.sample(koloda, 1)
        my.append(x[0])
        print(sum(my))
        if sum(my) > 21:
            game = 'stop'
            if sum(bot) < 15:
                y = random.sample(koloda, 1)
                bot.append(y[0])
            else:
                print('крупье закончил брать карты, Ваш ход')
    elif choice == 'нет':
        if sum(bot) < 15:
            y = random.sample(koloda, 1)
            bot.append(y[0])
        else:
            game = 'stop'
    else:
        print('скажите либо да либо нет')

#подсчёт очков
if sum(my) > 21:
    print('вы проиграли')
    print('ваши очки:', sum(my),'очки крупье:', sum(bot))
elif sum(bot) > 21:
    print('вы выиграли'),
    print('ваши очки:', sum(my),'очки крупье:', sum(bot))
else:
    if sum(my) > sum(bot):
        print('вы выиграли'),
        print('ваши очки:', sum(my), 'очки крупье:', sum(bot))
    else:
        print('вы проиграли')
        print('ваши очки:', sum(my), 'очки крупье:', sum(bot))