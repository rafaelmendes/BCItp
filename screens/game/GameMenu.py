from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from standards import *

class GameMenu(Screen):
# layout
    def __init__ (self, session_header,**kwargs):
        super (GameMenu, self).__init__(**kwargs)
        self.sh = session_header

        box1 = BoxLayout(size_hint_x=1, size_hint_y=0.5,padding=10, spacing=10, orientation='vertical')

        self.label_msg = Label(text="Game Menu", font_size=FONT_SIZE)

        button_start = Button(text="Start", size = BUTTON_SIZE)
        button_start.bind(on_press= self.change_to_acquisition)

        button_settings = Button(text="Settings", size = BUTTON_SIZE)
        button_settings.bind(on_press= self.change_to_gamesettings)

        button_back = Button(text="Back", size = BUTTON_SIZE)
        button_back.bind(on_press= self.change_to_bci)


        box1.add_widget(self.label_msg)

        box1.add_widget(button_start)
        box1.add_widget(button_settings)
        box1.add_widget(button_back)

        self.add_widget(box1)

    def change_to_acquisition(self,*args):
        self.manager.current = ''
        self.manager.transition.direction = 'left'

    def change_to_gamesettings(self,*args):
        self.manager.current = 'GameSettings'
        self.manager.transition.direction = 'left'

    def change_to_bci(self,*args):
        self.manager.current = 'BCIMenu'
        self.manager.transition.direction = 'right'