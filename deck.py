import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []

    #метод генерации колоды
    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))

    # метод пулла карты из колоды
    def pull(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    # метод подсчёта карт в колоде
    def count(self):
        return len(self.cards)
