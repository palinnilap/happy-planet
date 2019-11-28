
from player import Player
from level import Level
from typing import Tuple

class GameLoop:

    def __init__(self, player : Player, levels : Tuple[Level], start_lev):
        self._levels = levels
        self._player = player
        self._cur_lev_num = 0
        self._cur_lev = None
        self._status = 0  
            #  0  --> in progress
            #  1  --> won
            # -1  --> lost
        self._set_level (start_lev)

    @property
    def level_rgbs(self):
        if self._cur_lev_num == 0:
            return [.3,.3,.3,1], [.1,.1,.1,1]
        if self._cur_lev_num == 1:
            return [1,.8,.8,1], [.6,.4,.4,1]
        if self._cur_lev_num == 2:
            return [1,.4,.4,1], [.6,.3,.3,1]
        if self._cur_lev_num == 3:
            return [1,.1,.1,1], [.2,.2,.2,1]
        if self._cur_lev_num == 4:
            return [1,.8,0,1], [.7,0,0,1]

    @property
    def status(self):
        return self._status

    def get_next_challenge(self):
        return self._cur_lev.get_next_challenge()

    def submit_results(self, score : int, happy : int):
        self._player.add_score(score)
        self._player.add_happy(happy)
        self.check_happy()

    def check_happy(self):
        if self._player.happy <= 0:
            self._status = -1
        elif self._player.happy < 25:
            self._set_level(0)
        elif self._player.happy < 50:
            self._set_level(1)
        elif self._player.happy < 75:
            self._set_level(2)
        elif self._player.happy < 100:
            self._set_level(3)
        elif self._player.happy > 100:
            self._set_level(4)
            self._status = 1

    def get_score_happy(self):
        return str(self._player._score), str(self._player._happy)

    def _set_level(self, lev_num : int):
        self._cur_lev_num = lev_num
        self._cur_lev = self._levels[lev_num]
