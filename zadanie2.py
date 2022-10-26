# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import *


print('Да начнется ИГРА!')



def player_vs_player():
    total_goodies = 2021
    max_candy = 28
    count = 0
    player_1 = input('Как тебя зовут?: ')
    player_2 = input('А твоего соперника?: ')

    print(f'Ну, чтож {player_1} и {player_2}, начнем!')
    print('Для начала опеределим кто первый начнет игру.')

    x = randint(1, 2)
    if x == 1:
        winner = player_1
        loser = player_2
    else:
        winner = player_2
        loser = player_1
    print(f'Поздравляю, {winner} твой ход первый!')

    while total_goodies > 0:
        if count == 0:
            tmp = int(input(f'Сколько конфет, {winner}, ты хочешь взять?: '))
            while tmp > total_goodies or tmp > max_candy:
                tmp = int(input(f'Подумай снова {winner}: '))
            total_goodies = total_goodies - tmp
        if total_goodies > 0:
            print(f'Отлично, осталось {total_goodies} конфет')
            count = 1
        else:
            print('Вкусняшки закончились')

        if count == 1:
            tmp = int(input(f'Ооо,твой ход, {loser}: '))
            while tmp > total_goodies or tmp > max_candy:
                tmp = int(input(f'Давай-ка еще разик, {loser}: '))
            total_goodies = total_goodies - tmp
        if total_goodies > 0:
            print(f'Круть! Еще {total_goodies} вкусняшек')
            count = 0
        else:
            print('Вкусняшки тю-тю')

    if count == 0:
        print(f'{winner} ПОБЕДИЛ')
    if count == 1:
        print(f'{loser} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    total_goodies = 2021
    max_candy = 28
    player_1 = input('Как тебя зовут?: ')
    player_2 = 'КОМПЬЮТЕР'
    players = [player_1, player_2]
    print(f'{player_1} и {player_2}, приступим. Удачи игрокам!')
    print('Для начала опеределим кто первый начнет игру.')

    winner = randint(-1, 0)

    print(f'Поздравляю, {players[winner+1]}, ты ходишь первым !')

    while total_goodies > 0:
        winner += 1

        if players[winner % 2] == 'КОМПЬЮТЕР':
            print(f'И так, {players[winner%2]}. Осталось {total_goodies} вкуснях. Сколько возьмешь?: ', end = ' ')
            
            if total_goodies < 29:
                tmp = total_goodies
            else:
                remain = total_goodies//28
                tmp = total_goodies - ((remain*max_candy)+1)
                if tmp == -1:
                    tmp = max_candy -1
                if tmp == 0:
                    tmp = max_candy
            while tmp > 28 or tmp < 1:
                tmp = randint(1,28)
            print(tmp)
        else:
            tmp = int(input(f'Ну чтож, {players[winner%2]}, твой шаг:  '))
            while tmp > max_candy or tmp > total_goodies:
                tmp = int(input(f'За раз не более {max_candy} конфет, попробуем снова: '))
        total_goodies = total_goodies - tmp

    print(f'В банке осталось {total_goodies} \nПобедил {players[winner%2]}')

player_vs_bot()
                                                                                                                