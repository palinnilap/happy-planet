from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    ObjectProperty
)
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class HappyGame(Widget):
    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    button3 = ObjectProperty(None)
    button4 = ObjectProperty(None)

    def update(self, dt):
        pass

    def on_touch_down(self, touch):
        if self.button1.collide_point(*touch.pos):
            print('button1 pushed')
        elif self.button2.collide_point(*touch.pos):
            print('button2 pushed')
        elif self.button3.collide_point(*touch.pos):
            print('button3 pushed')
        elif self.button4.collide_point(*touch.pos):
            print('button4 pushed')
    
class HappyApp(App):
    def build(self):
        game = HappyGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    HappyApp().run()
