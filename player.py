from deck import Deck

class Player:
    def __init__(self, isDealer, deck):
        self.cards = []
        self.isDealer = isDealer
        self.deck = deck
        self.score = 0

    #метод хода игрока
    def take(self):
        self.cards.extend(self.deck.pull(1))
        self.check_score()
        if self.score > 21:
            return 1
        return 0

    #метод розыгрыша
    def deal(self):
        self.cards.extend(self.deck.pull(2))
        self.check_score()
        if self.score == 21:
            return 1
        return 0

    #метод проверка счёта
    def check_score(self):
        a_counter = 0
        self.score = 0
        for card in self.cards:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()

        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    #метод показа карт на руках
    def show(self, start=False):

        if self.isDealer:
            print("Карты дилера")
            if start:
                self.cards[0].show(True)
                self.cards[1].show()
                return

        else:
            print("Ваши карты")

        for i in self.cards:
            i.show()

        print("Счёт: " + str(self.score))