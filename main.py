from deck import Deck
from player import Player
from game import Game
from bank import Bank
import keyboard
import time

if __name__ == '__main__':
    black_jack = Game()
    print('Добро пожаловать в игру Блек-Джек. Нажмите enter, чтобы начать или q, чтобы выйти: ')
    key = keyboard.read_key()
    if key == 'enter':
        print(f'Ваш баланс: {Bank.points_left} ')
        time.sleep(1)
        black_jack.play()
    while key != 'q':
        time.sleep(1)
        if Bank.is_lost:
            print("Ваш банк теперь пусть. Перезапустите приложение, чтобы сыграть снова")
            break

        print('Чтобы продолжить, нажмите enter или q, чтобы выйти: ')
        key = keyboard.read_key()
        if key == 'enter':
            black_jack.play()




