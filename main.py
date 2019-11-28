from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    ObjectProperty, StringProperty
)
from kivy.clock import Clock
import factory
import time

class HappyGame(Widget):
    BUTTON_DN = [.5,.5,.5,1]
    BUTTON_UP = [1,1,1,1]
    BUTTON_DISABLED = [0,0,0,0]
    
    #uix elements
    score = ObjectProperty(None)
    happy_meter = ObjectProperty(None)
    score_updater = ObjectProperty(None)
    prompt = ObjectProperty(None) 
    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    button3 = ObjectProperty(None)
    button4 = ObjectProperty(None)

    #class stats
    PRESSED = 0
    CONTINUE = 0
    BUTTON_ENBLD = 1

    #setup gameloop
    gameloop = factory.create_gameloop()
    cur_challenge = gameloop.get_next_challenge()

    def update(self, dt):
        '''main cycle for reacting to user input'''
        if self.prompt.text == 'error':  
            #need to set up intial values
            self.set_scores()
            self.populate_challenge()

        if self.CONTINUE and self.PRESSED == 1:
            self.cur_challenge = self.gameloop.get_next_challenge()
            self.score_updater.text = ''
            self.populate_challenge()
            self.CONTINUE = 0
            self.PRESSED = 0
            
        if self.PRESSED and not self.CONTINUE:
            self.hide_unpicked_buttons()
            self.prompt.text = ''
            
            self.BUTTON_ENBLD = 0
            self.CONTINUE = 1
            
            self.process_choice()
            self.PRESSED = 0
            
    
    def process_choice(self) -> None:
        val, expl = self.cur_challenge.asses_choice(self.PRESSED)
        self.gameloop.submit_results(1, val) #score always increments by 1
        Clock.schedule_once(lambda dt: self.display_score_update(val), 1)
        Clock.schedule_once(lambda dt: self.display_expl(expl), 2)
        Clock.schedule_once(
            lambda dt: self.set_scores(), 4
        )
        Clock.schedule_once(
            lambda dt: self.set_buttons_to_continue(), 6
        )
        Clock.schedule_once(
            lambda dt: self.enable_buttons(), 6
        )

    def hide_unpicked_buttons(self):
        if not self.PRESSED == 1:
            self.button1.text = ''
        if not self.PRESSED == 2:
            self.button2.text = ''
        if not self.PRESSED == 3:
            self.button3.text = ''
        if not self.PRESSED == 4:
            self.button4.text = ''
             
    def enable_buttons(self):
        self.BUTTON_ENBLD = 1
    def display_score_update(self, val):
        self.score_updater.text = self.format_val(val)
    def display_expl(self, expl):
        self.prompt.text = expl

    def set_buttons_to_continue(self):
        
        self.button1.text = "Continue"
        self.button2.text = ''
        self.button3.text = ''
        self.button4.text = ''       

    def format_val(self, val : int) -> None:
        if val >= 0:
            return '+' + str(val)
        
        else:
            return str(val)

    def set_scores(self) -> None:
        score, happy = self.gameloop.get_score_happy()
        self.score.text = score
        self.happy_meter.text = happy 

    def populate_challenge(self) -> None:
        self.prompt.text = self.cur_challenge.get_prompt()
        self.button1.text = self.cur_challenge.get_choices()[0]
        self.button2.text = self.cur_challenge.get_choices()[1]
        self.button3.text = self.cur_challenge.get_choices()[2]
        self.button4.text = self.cur_challenge.get_choices()[3]

        if self.cur_challenge.get_choices()[0] = '':
            self.button1.background_color = self.BUTTON_DISABLED
        if self.cur_challenge.get_choices()[1] = '':
            self.button2.background_color = self.BUTTON_DISABLED
        if self.cur_challenge.get_choices()[2] = '':
            self.button3.background_color = self.BUTTON_DISABLED
        if self.cur_challenge.get_choices()[3] = '':
            self.button4.background_color = self.BUTTON_DISABLED
        
    def on_touch_down(self, touch):
        '''lets self.update know which button was pressed. changes color'''
        # this code is not DRY. kv language made simpler code hard to write
        if not self.BUTTON_ENBLD:
            return
        if self.button1.collide_point(*touch.pos):
            self.PRESSED = 1
            self.button1.background_color = self.BUTTON_DN
        elif self.button2.collide_point(*touch.pos):
            self.PRESSED = 2
            self.button2.background_color = self.BUTTON_DN
        elif self.button3.collide_point(*touch.pos):
            self.PRESSED = 3 
            self.button3.background_color = self.BUTTON_DN
        elif self.button4.collide_point(*touch.pos):
            self.PRESSED = 4
            self.button4.background_color = self.BUTTON_DN
    
    def on_touch_up(self, touch):
        '''turns all buttons back to default color'''
        self.button1.background_color = self.BUTTON_UP
        self.button2.background_color = self.BUTTON_UP
        self.button3.background_color = self.BUTTON_UP
        self.button4.background_color = self.BUTTON_UP
            
class HappyApp(App):
    def build(self):
        game = HappyGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    HappyApp().run()
