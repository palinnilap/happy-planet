from challenge import Challenge
from level import Level, LevelSequential
from player import Player
from gameloop import GameLoop

def create_gameloop():
    player = Player(-2019)
    levels = (create_level_0(), create_level_1(), create_level_2(), create_level_3())
    return GameLoop(player, levels, 1, create_tut_lev(), create_won_lev(), create_lost_lev())

def create_level_0():
    challenges = (
        challenge00(), challenge01(), challenge02(), challenge03()
    )
    return Level(challenges)

def create_level_1():
    challenges = (
        challenge11(), challenge12(), challenge13()
    )
    return Level(challenges)

def create_level_2():
    challenges = (
        challenge20(), challenge21(), challenge22()
    )
    return Level(challenges)

def create_level_3():
    challenges = (
        challenge30(), challenge31(), challenge32(), challenge33()
    )
    return Level(challenges)

def create_tut_lev():
    challenges = (
        challenge_t0(), challenge_t1()
    )
    return LevelSequential(challenges)

def create_lost_lev():
    challenges = (
        challenge_lost0()
    )
    return LevelSequential(challenges)

def create_won_lev():
    challenges = (
        challenge_won0()
    )
    return LevelSequential(challenges)


############ level 0 #############################

def challenge00():
    prompt = '''Your mood is low. 
    You feel so sad even snuggling a baby bulldog wouldn't cheer you up.
    What do you do?'''
    choices = ('Call Stan', 'Eat something', 'Fetal position', 'Pep talk')
    ans_vals = (-10,3,3,-10)
    ans_expl =  (
        'Stan doesn\'t like you.', 
        'You feel your strength reviving...', 
        'What doesn\'t kill you makes you stronger?',
        'Your best try quickly soured into you listing reasons mold is more likeable than you are.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge01():
    prompt = '''Your mood is low.\n
MovieFlix just released all 4 seasons of "Pathetic People with Lives You Will Enjoy Judging".'''
    choices = ('Sounds like a plan!', 'I\'m going to train for a marathon instead!',
              'I\'ll take a walk first', 'I\'ll go outside. To do what, I don\'t know.')
    ans_vals = (-8,-10,5,5)
    ans_expl =  (
        'You have melted into a puddle on the couch. No one is quite sure where you end and butt-imprinted foam begins.', 
        'You put on running shoes, decided you would never be able to do it, and then watched movies with shoes on', 
        'Good choice!',
        'Anything is better than nothing!'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge02():
    prompt = '''Your mood is low.\n
    You just realized you spent the last 3 hours thinking about how jealous you are of house plants. What in the world are you going to do next?'''
    choices = ('Take it one day at a time', 'Take it one hour at a time',
              'Take it one minute at a time', 'Take it 10 seconds at a time')
    ans_vals = (1,2,3,-1)
    ans_expl =  (
        'Let tomorrow worry about itself!', 
        'Small steps!', 
        'Just got through another minute!',
        'You tried, but forgot the word for 7 and gave up.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge03():
    prompt = '''Your mood is low.\n\nYou are always talking to yourself. What are you saying right now?'''
    choices = ('I have the personality of a sponge', 
        'I\'m pretty sure the only reason my friends like me is because I have a pogo stick.',
        'I wish my face was a pogo stick', 'Life is like my underwear. It doesn\'nt change.')
    ans_vals = (-1,-1,-1,-1)
    ans_expl =  (
        'Oddly enough, so do sponges.', 
        'Imagine if you DID\'NT have that pogo stick then.', 
        'That is the weirdest thing I have ever heard.',
        'Bruh, change them drawers.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)


############ level 1 #############################


def challenge11():
    prompt1 = 'What a nice day!\n\nWhat would you like to do?'
    choices1 = ('Smile', 'Laugh', 'Hugs', 'Cry')
    ans_vals1 = (3,5,-10,-5)
    ans_expl1 =  (
        "Show them pearls!", 
        'The best medicine!\n\n(this statement has not been approved by the FDA)',
        'You chose a bear.\nFrom now on, your hugs will all be one-armed.',
        'Well, you haven\'t quite gotten the hang of this game yet...'
    ) 
    return Challenge(prompt1, choices1, ans_vals1, ans_expl1)

def challenge12():
    prompt1 = 'I KNOW. Let\'s do something for four hours straight!'
    choices1 = ('Ski', 'Scream', 'Video Games', 'Read a biography, help orphans, and write well-informed letters to congress')
    ans_vals1 = (-5,7,-10,-1)
    ans_expl1 =  (
        "You had fun for 3 hours and 15 minutes. At 3 hours and 16 minutes you swerved to avoid a moose, went off a ledge, and landed on top of a CIA operative, thus blowing his cover. Oh. And you broke your collar bone.", 
        'Your shrieks were heard by a famous metal band. They offer you a lucrative contract.',
        'You won the MMORPG battle, but lost the afternoon',
        'No points awarded to the brown-noser.\n\nAnd, minus 1 points for lying.'
    ) 
    return Challenge(prompt1, choices1, ans_vals1, ans_expl1)

def challenge13():
    prompt1 = 'Time to pick a name for your new band.'
    choices1 = ('Shredder Kitties', 'AC/Defroster', 'Shotguns and Petunias', 'Steel Dirgible')
    ans_vals1 = (5,3,-5,1)
    ans_expl1 =  (
        'Solid choice.\n\nYou captured both your unbridled rage and cuddly inner soul.', 
        'Familiar but catchy.',
        'Your first single: "Welcome to the Forest"\n\n was not a hit',
        'Definitely better than your runner up choice:\n\n "The Stink Beatles"'
    ) 
    return Challenge(prompt1, choices1, ans_vals1, ans_expl1)
############ level 2 #############################

def challenge20():
    prompt1 = 'Is it just me, or is it getting AWESOME in here?'
    choices1 = ('It\'s just you', 'Did someone open up a can of YEEEHAAA?', 
            'I heard on the radio that today it will be sunny with a chance of SHABAM!', 
            'Let\'s blast some country music!!'
    )
    ans_vals1 = (-5,5,5,-10)
    ans_expl1 =  (
        'Party pooper\n >:|', 
        'YOU\'RE DARN RIGHT I DID',
        'Are you a tornado? \'Cause you raisin\' the roof!',
        'How about let\'s not'
    ) 
    return Challenge(prompt1, choices1, ans_vals1, ans_expl1)

def challenge21():
    prompt = ('''"Ridonculous" took the civil world by storm. "Classic" took a fine word and made it on point.\n
              What's the next annoying phrase you will grace humanity with?''')
    choices = ('Spectankulous', 'Counterfactual', 'Tiktoktakular', 'Typey')
    ans_vals = (5,7,-10,8)
    ans_expl =  (
        'Nerdy high schoolers everywhere thank you for giving them something they think will make them sound cool', 
        'PRENTENSION LEVEL UP. You sound crazy smart without actually having to know what the word means because you are using it "ironically."',
        'Sorry, not that creative. Plus China is spying on you.',
        'What\'s old? Typewriters. See that guy looking at a map? That is SO typey.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge22():
    prompt = ('''You are about to get on an airplane to sign a disarmament treaty with North Korea
     when you hear some CRANKED UP music and the sounds of people dancing in the distance.''')
    choices = ('Treaty Smeaty. Dance is life.', 'Call me Kim Jung Una FIESTA DE BAILE', 
        '“Without delayed gratification, there is no power over self.”', 
        'The greatest joy is a job well done'
    )
    ans_vals = (3,2,-10,0)
    ans_expl =  (
        'NO JOY IS REAL BUT THE PRESENT!', 
        'Is that confetti? Oh, it\'s nuclear ash? HEY SARAH, WE DON\'T NEED GLOWSTICKS ANYMORE. YEAH, wE ArE ABOuT to BECOme GLoW hUMANS',
        'Did you go to college? Because it sounds like you have a bachelor\'s degree in BORING.',
        'Life\'s uncertain. Eat dessert first.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

#People are having so much fun, but they are hipsters. What will you do to get in?

############ level 3 #############################

def challenge30():
    prompt = ('''Man, you are SO FREAKIN\' EXCITED\n
                How are you going to take this to the next level?''')
    choices = ('Eat cake', 'Punch a clown', 'Eat ice cream ALL DAY', 'Be Yourself')
    ans_vals = (2,7,-10,-20)
    ans_expl =  (
        "SUGAR RUSH!!!!!!!!!!", 
        'How can something that feels so right be wrong?',
        'Diarrhea\n :`(',
        'Not to be offensive, but everyone you know is worse off for having known you.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge31():
    prompt = ('''ARE. YOU. HAPPY. YET?!''')
    choices = ('Yes', 'YHEEESSSS', 'No', 'I\'m only getting started')
    ans_vals = (1,-10,5,-5)
    ans_expl =  (
        'WHERE IS THE PASSION?', 
        'CAN YOU EVEN SPELL?!',
        'THAT\'S RIGHT. NEVER BE CONTENT! Compared to how happy you GONNA BE, THIS IS NOTHING YET!!!!!',
        'THEN START FOR REAL, BRO.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge32():
    prompt = ('''WHAT IS THE PURPOSE OF LIFE?!!!''')
    choices = ('Be happy','Make a meaningful impact on the world', 
            'Become famous', 'DIE WITH MORE MONEY THAN GOD.')
    ans_vals = (5,-5,-5,-5)
    ans_expl =  (
        'A THOUSAND TIMES YES. NOTHING ELSE MATTERS.', 
        'But what if you are crying while you do it? Then what is it worth?!',
        'FAMOUS PEOPLE DON\'T LOOK HAPPY TO ME',
        'IF YOU ARE GOING TO DIE, IT WILL ONLY BE FROM BEING TOO HAPPY.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge33():
    prompt = '''You are RUNNING through the streets SHOUTING FOR JOY and you see someone NOT looking COMPLETELY ENTHUSED about life.'''
    choices = ('Give him a high-five', 
    'SCREAM in his face like A DRILL SERGEANT OF HAPPINESS until FEELS THE HAPPYS to the core of his middle-aged being', 
    'Punch him on the shoulder and say, "JOY BUGGY"', 
    'Keep walking. Don\'t let him vampire your joy.')
    ans_vals = (0,5,2,-10)
    ans_expl =  (
        'He did not give you a high five back. Your face burns with the indignation of unrequited love.', 
        'DON\'T YOU SEE THE HAPPYS YOU ARE MISSING?! QUITE YOUR JOB. EAT TWINKIES UNTIL YOU PUKE. DO WHATEVER YOU MUST TO ACQUIRE LOLS',
        'Great idea, but it didn\'t do enough. PUNCH HIM AGAIN UNTIL HE FEELS THE LOVE',
        'NO. NO ONE CAN MISS OUT ON THIS. THEY MUST FEEL THE JOY.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

############ Tutorial #############################

def challenge_t0():
    prompt = ('''H  A  P  P  Y \n\nP  L  A  N  E  T''')
    choices = ('', '', '', 'continue')
    ans_vals = (0,0,0,0)
    ans_expl =  (
        '', 
        '',
        '',
        'by palinnilap and dragongirl'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

def challenge_t1():
    prompt = ('''You will be given 25 mood to start.\n\n
    Don\'t screw this up.''')
    choices = ('', '', 'Start Game', '')
    ans_vals = (0,0,2019+25,0)
    ans_expl =  (
        '', 
        '',
        'Time to make the world a happy place',
        ''
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

############ Lost #############################

def challenge_lost0():
    prompt = ('''Congratulations. You lost.''')
    choices = ('', '', '', 'I want to try again.')
    ans_vals = (0,0,0,0)
    ans_expl =  (
        '', 
        '',
        '',
        'What about "you lost" was hard to understand?'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)

############ Won #############################

def challenge_won0():
    prompt = ('''Congratulations. You won. But unfortunately, the programmer hasn't put the awesome stuff here he planned to yet.''')
    choices = ('', '', '', 'I am the best.')
    ans_vals = (0,0,0,0)
    ans_expl =  (
        '', 
        '',
        '',
        'Yes, our jolly monarch, you are.'
    ) 
    return Challenge(prompt, choices, ans_vals, ans_expl)