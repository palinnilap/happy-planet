from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    ObjectProperty, StringProperty
)
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class HappyGame(Widget):
    HALF_GREY = [.5,.5,.5,1]
    FULL_GREY = [1,1,1,1]
    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    button3 = ObjectProperty(None)
    button4 = ObjectProperty(None)

    def update(self, dt):
        pass

    def on_touch_down(self, touch):
        if self.button1.collide_point(*touch.pos):
            self.button1.background_color = self.HALF_GREY
            
        elif self.button2.collide_point(*touch.pos):
            self.button2.background_color = self.HALF_GREY
        elif self.button3.collide_point(*touch.pos):
            self.button3.background_color = self.HALF_GREY
        elif self.button4.collide_point(*touch.pos):
            self.button4.background_color = self.HALF_GREY
    
    def on_touch_up(self, touch):
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
