
from challenge import Challenge
from level import Level
from player import Player
from gameloop import GameLoop

def create_gameloop():
    player = Player(25)
    levels = (create_level_1(), 'fake')
    return GameLoop(player, levels, 0)

def create_level_1():
    prompt1 = ('What a nice day!\nWhat would you like to do?')
    choices1 = ('Smile', 'Laugh', 'Hugs', 'Yays')
    ans_vals1 = (3,5,-10,0)
    ans_expl1 =  (
        "Show them pearls!", 
        'The best medicine!\n(this statement has not been approved by the FDA)',
        'You chose a bear. One armed hugs are all you are giving from now on.',
        'Some people do not have it as good as you, be more thoughtful.'
    ) 
    challenge1 = Challenge(prompt1, choices1, ans_vals1, ans_expl1)
    
    challenges = (
        challenge1,

    )

    return Level(challenges)


# Dragongirl Gaming <livery2007@gmail.com>
# #Are you happy yet?
# import time
# import random

# class Questions:
#     Q_LIST = [   
# [   #Level 0
#     ['1. Smile', 3, "Show them pearls!"],
#     ['2. Laugh', 5, 'The best medicine! (this statement has not been approved by the FDA)'],
#     ['3. Hugs', -10, 'You chose a bear. One armed hugs are all you are giving from now on.'],
#     ['4. Yays', 0, 'Some people do not have it as good as you, be more thoughtful.'],
# ],
# [   #Level 1
#     ['1. Jump', -1, "How was the last book of Hairy Hopper? I heard he scraped his knee. So did you."],
#     ['2. Ski', -5, 'You broke a bone. That wouldn\'t make me happy.'],
#     ['3. Video Gaming', -15, 'Your mom gave you permanant screen time. Yeesh.'],
#     ['4. Doctor', 10, 'Your Doctor gave you something that will give you more happiness! Bet you didn\'t see that coming.'],
# ],
# [   #Level 2
#     ['1. Eat Cake', 10, "SUGAR RUSH!!!!!!!!!!"],
#     ['2. Punch a Clown', 7, 'How can something that feels so right be wrong?'],
#     ['3. Eat Icecream ALL DAY', -10, 'Diarrhea :(.'],
#     ['4. Be Yourself', -20, 'Not to be offensive, but everyone you know is worse off for having known you.'],
# ],
# [   #Level 3
#     ['1. Eat Cake', 10, "SUGAR RUSH!!!!!!!!!!"],
#     ['2. Punch a Clown', 7, 'How can something that feels so right be wrong?'],
#     ['3. Eat Icecream ALL DAY', -10, 'Diarrhea :(.'],
#     ['4. Be Yourself', -20, 'Not to be offensive, but everyone you know is worse off for having known you.'],
# ],
    