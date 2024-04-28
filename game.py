import bank
from deck import Deck
from player import Player
from accessify import private
from bank import Bank
import time


class Game:
    def __init__(self):
        self.set_up()

    # метод сетапа игры
    @private
    def set_up(self):
        self.deck = Deck()
        self.bank = Bank()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    # основной метод игры
    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()
        input()
        curr_bet = 0
        while curr_bet > self.bank.points_left or curr_bet == 0:
            curr_bet = float(input("Сделайте ставку: "))
            if curr_bet > self.bank.points_left or curr_bet == 0:
                print("Вы не можете поставить ставку, превышающую ваш баланс или не поставить ничего")

        self.bank.bet(curr_bet)

        print(f"Ваша ставка: {curr_bet}")
        time.sleep(2)
        self.player.show()
        time.sleep(2)
        self.dealer.show(True)

        if p_status == 1:
            self.bank.win()
            print(f"Вы победили. Поздравляем! Ваш баланс: {self.bank.points_left}")

            if d_status == 1:
                print(f"У вас ничья. Ваш баланс: {self.bank.points_left}")
            return 1

        cmd = ""
        while cmd != "хватит":
            bust = 0
            cmd = input("Ещё, хватит или повысить ставку? ").lower()

            if cmd == "ещё":
                bust = self.player.take()
                self.player.show()
            if cmd == "повысить ставку":
                if not self.bank.is_increased:
                    sum = int(input("Введите сумму: "))
                    self.bank.increase_bet(sum)
                    bust = self.player.take()
                    self.player.show()
                else:
                    print("Вы уже повышали ставку")

            if bust == 1:
                print(f"К сожалению, вы проиграли. Ваш баланс: {self.bank.points_left}")
                return 1
        print("\n")
        time.sleep(2)
        self.dealer.show()
        if d_status == 1:
            self.bank.lose()
            print(f"Дилер сразу же победил! Удачи в следующий раз! Ваш баланс: {self.bank.points_left}")
            return 1

        while self.dealer.check_score() < 17:
            if self.dealer.take() == 1:
                time.sleep(2)
                self.dealer.show()
                self.bank.win()
                print(f"Дилер проиграл. Поздравляем! Ваш баланс: {self.bank.points_left}")
                return 1
            time.sleep(2)
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print(f"У вас ничья. Ваш баланс: {self.bank.points_left}")
        elif self.dealer.check_score() > self.player.check_score():
            self.bank.lose()
            print(f"Дилер победил. Была хорошая игра! Ваш баланс: {self.bank.points_left}")
        elif self.dealer.check_score() < self.player.check_score():
            self.bank.win()
            print(f"Вы победили! Ваш баланс: {self.bank.points_left}")

        self.set_up()



