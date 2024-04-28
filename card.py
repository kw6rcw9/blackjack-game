class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value - 1]
        self.suit = '♥♦♣♠'[suit]

    #метод рисунка карты
    def show(self, is_dealer=False):
        val = self.value
        type_of_card = self.suit

        if is_dealer:
            val = '?'
            type_of_card = '?'

        print('┌───────┐')
        print(f'| {val:<2}    |')
        print('|       |')
        print(f'|   {type_of_card}   |')
        print('|       |')
        print(f'|    {val:>2} |')
        print('└───────┘')
    #метод счёта очков за карту
    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost