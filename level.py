
import random

class Level:

    def __init__(self, challenge_tup):
        self.challenge_tup = challenge_tup

    def get_next_challenge(self):
        return self.challenge_tup[
            random.randrange(0, len(self.challenge_tup))
        ]