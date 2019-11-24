from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    ObjectProperty, StringProperty
)
from kivy.clock import Clock

class HappyGame(Widget):
    HALF_GREY = [.5,.5,.5,1]
    FULL_GREY = [1,1,1,1]
    PRESSED = 0
    score = ObjectProperty(None)
    happy_meter = ObjectProperty(None)
    prompt = ObjectProperty(None) 
    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    button3 = ObjectProperty(None)
    button4 = ObjectProperty(None)

    def update(self, dt):
        '''main cycle for reacting to user input'''
        if self.PRESSED:
            self.prompt.text = ('button ' + str(self.PRESSED) + ' was pressed')
            self.PRESSED = 0

    def on_touch_down(self, touch):
        '''lets update know which button was pressed and changes color'''
        # this code is not DRY. kv language made simpler code hard to write
        if (self.button1.collide_point(*touch.pos)
        # and challenge.prompt[1] != ""
        ):
            self.PRESSED = 1
            self.button1.background_color = self.HALF_GREY
        elif self.button2.collide_point(*touch.pos):
            self.PRESSED = 2
            self.button2.background_color = self.HALF_GREY
        elif self.button3.collide_point(*touch.pos):
            self.PRESSED = 3 
            self.button3.background_color = self.HALF_GREY
        elif self.button4.collide_point(*touch.pos):
            self.PRESSED = 4
            self.button4.background_color = self.HALF_GREY
    
    def on_touch_up(self, touch):
        '''turns all buttons back to default color'''
        self.button1.background_color = self.FULL_GREY
        self.button2.background_color = self.FULL_GREY
        self.button3.background_color = self.FULL_GREY
        self.button4.background_color = self.FULL_GREY
            
class HappyApp(App):
    def build(self):
        game = HappyGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    HappyApp().run()
