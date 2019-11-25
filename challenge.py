
from typing import Tuple

class Challenge:
    
    def __init__(
        self, prompt : Tuple[str], 
        choices : Tuple[str],
        ans_vals : Tuple[int],
        ans_expl : Tuple[str]
    ):
        self._prompt = prompt
        self._choices = choices
        self._ans_vals = ans_vals
        self._ans_expl = ans_expl

    def get_prompt(self) -> tuple:
        return self._prompt

    def get_choices(self) -> tuple:
        return self._choices
    
    def asses_choice(self, choice : int):
        choice -= 1  #tuples are zero indexed
        return self._ans_vals[choice], self._ans_expl[choice]
