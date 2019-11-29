
from random import randrange
from typing import Tuple
from challenge import Challenge

class Level:

    def __init__(self, challenges : Tuple[Challenge]):
        self._challenges = challenges

    def get_next_challenge(self):
        rand = randrange(0, len(self._challenges))
        return self._challenges[rand]

class LevelSequential(Level):
    CURRENT = 0

    def get_next_challenge(self):
        challenge = self._challenges[self.CURRENT]
        
        #in order to avoid an indexing error
        if len(self._challenges) - 1 > self.CURRENT:
            self.CURRENT += 1

        return challenge