# Sponsered ny Nike


class Nike:

    def __init__(self, acceleration):
        self.acceleration = acceleration
        self.location = 0


class Footrace:

    def __init__(self, distance):
        self.distance = distance
        self.nikes = []

    def add_nike(self, nike):
        self.nikes.append(nike)

    def add_nikes(self, nike_list):
        for nike in nike_list:
            self.add_nike(nike)

    def tick(self):
        for nike in self.nikes:
            nike.location += nike.acceleration

    def has_won(self):
        for nike in self.nikes:
            if nike.location >= self.distance:
                self.winner = nike
                return True
        return False
