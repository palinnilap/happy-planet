

class Player():

    def __init__(self, start_happy):
        self._happy = start_happy
        self._score = 0

    def add_happy(self, val):
        self._happy += val
    
    def add_score(self, val):
        self._score += val

    @property
    def happy(self):
        return self._happy