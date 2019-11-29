
from player import Player
from level import Level
from typing import Tuple

class GameLoop:

    def __init__(self, 
        player : Player, 
        main_levels : Tuple[Level], start_lev, 
        lev_tutorial=None, lev_won=None, lev_lost=None):
        self._levels = main_levels
        self._player = player
        self._cur_lev_num = 0
        self._cur_lev = None
        self._level_won = lev_won
        self._level_lost = lev_lost
        self._status = 0  
            #  0  --> in progress
            #  1  --> won
            # -1  --> lost
        self._set_level (start_lev)

    @property
    def level_rgbs(self):
        return self._get_rgbs()
        
    @property
    def status(self):
        return self._status

    @property
    def score(self):
        return str(self._player._score)
    
    @property
    def emoji(self):
        return self._get_emoji()

    @property
    def happy(self):
        return str(self._player._happy)


    def get_next_challenge(self):
        return self._cur_lev.get_next_challenge()

    def submit_results(self, score : int, happy : int):
        self._player.add_score(score)
        self._player.add_happy(happy)
        self.check_happy()

    def check_happy(self):
        if self._player.happy <= 0:
            self._change_status(-1)
        elif self._player.happy < 25:
            self._set_level(0)
        elif self._player.happy < 50:
            self._set_level(1)
        elif self._player.happy < 75:
            self._set_level(2)
        elif self._player.happy < 100:
            self._set_level(3)
        elif self._player.happy > 100:
            self._change_status(1)

    def _set_level(self, lev_num : int):
        self._cur_lev_num = lev_num
        self._cur_lev = self._levels[lev_num]

    def _change_status(self, to_what : int):
        self._status = to_what
        if to_what == 1:
            self._cur_lev_num = 100
            self._cur_lev = self._level_won
        elif to_what == -1:
            self._cur_lev_num = -1
            self._cur_lev = self._level_lost

    def _get_rgbs(self):
        if self._status == -1:  #lost
            return [.1,.1,.5,1], [0,0,.2,1]
        elif self._status == 1:  #won
            return [1,.8,0,1], [.7,0,0,1]

        elif self._cur_lev_num == 0:
            return [.2,.2,.5,1], [.1,.1,.3,1]
        elif self._cur_lev_num == 1:
            return [1,.8,.8,1], [.6,.4,.4,1]
        elif self._cur_lev_num == 2:
            return [1,.4,.4,1], [.6,.3,.3,1]
        elif self._cur_lev_num == 3:
            return [1,.1,.1,1], [.2,.2,.2,1]

    def _get_emoji(self):
        if self._player._happy < 10:
            return r'.·´¯`(>_<)´¯`·.'
        elif self._player._happy < 25:
            return r'¯\_(•_•)_/¯'
        elif self._player._happy < 50:
            return '(•_•)'
        elif self._player._happy < 75:
            return '(^__^)'
        elif self._player._happy >= 75:
            return r'¯\(^__^)/¯'


#kivy apparently doesn't deal well with unicode characters :(
# r'''
# ( ಥ_ಥ )
# ¯\_(⊙︿⊙)_/¯
# (;︵;)
# .·´¯`(>▂<)´¯`·.
# (ၜ︗ၜ) 
# ლ(ಠ_ಠლ)

# (⨪_⨪)
# (•_•)
# (◉ܫ◉)
# (•ᴗ•)

# (ၜᗝ ၜ) 
# (^ ᗜ ^)
# (◕‿◕✿)
# ( ဖ ͜ စ)

# (ꙨပꙨ)
# (^‿^)
# (◉⩊◉)
# (•̀ᴗ•́)و

# (≧ ᗜ ≦)
# ᕦ(ò_óˇ)ᕤ
# (⊙_◎)
# (ↈ_ↈ)
# '''