class Bank:

    points_left = 5000
    is_lost = False
    is_increased = False

    def __init__(self):
        self.current_bet = 0

    def bet(self, num: float):
        self.current_bet += num

    def lose(self):
        Bank.points_left -= self.current_bet
        if Bank.points_left <= 0:
            Bank.points_left = 0
            Bank.is_lost = True

    def win(self):
        self.points_left += self.current_bet

    def increase_bet(self, num: float):
        self.current_bet += num
        Bank.is_increased = True
