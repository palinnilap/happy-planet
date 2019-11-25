
from player import Player
from level import Level
from typing import Tuple

class GameLoop:

    def __init__(self, player : Player, levels : Tuple[Level], start_lev):
        self._levels = levels
        self._player = player
        self._cur_lev_num = start_lev
        self._cur_lev = self._levels[self._cur_lev_num]

    def get_next_challenge(self):
        return self._cur_lev.get_next_challenge()

    def submit_results(self, score : int, happy : int):
        self._player.add_score(score)
        self._player.add_happy(happy)
        self.check_happy()

    def check_happy(self):
        pass

        

