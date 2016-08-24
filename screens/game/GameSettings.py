############################## DEPENDENCIES ##########################
# KIVY modules:
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, ReferenceListProperty, \
                            ListProperty, BooleanProperty
from kivy.lang import Builder

# KV file:
Builder.load_file('screens/game/gamesettings.kv')

# Generic:

# Project's:
from standards import *
######################################################################


class GameSettings(Screen):

# layout
    def __init__ (self, session_header,**kwargs):
        super (GameSettings, self).__init__(**kwargs)
        self.sh = session_header

    def change_to_game(self,*args):

        self.manager.current = 'GameMenu'
        self.manager.transition.direction = 'right'

    def save_config(self,*args):

        ids = self.ids

        self.sh.game.game_threshold = ids.game_threshold.value
        self.sh.game.window_overlap = ids.window_overlap.value / 1000.0
        self.sh.game.warning_threshold = ids.warning_threshold.value 
        self.sh.game.forward_speed = ids.forward_speed.value / 1000.0
        self.sh.game.inst_prob = ids.inst_prob.value / 1000.0
        self.sh.game.keyb_enable = ids.keyb_enable.value 

        self.sh.game.flag = True
        self.sh.saveToPkl()

    def update_settings(self):

        ids = self.ids

        ids.game_threshold.value = self.sh.game.game_threshold
        ids.window_overlap.value = self.sh.game.window_overlap * 1000
        ids.warning_threshold.value  = self.sh.game.warning_threshold
        ids.forward_speed.value = self.sh.game.forward_speed * 1000.0
        ids.inst_prob.value = self.sh.game.inst_prob * 1000.0
        ids.keyb_enable.value  = self.sh.game.keyb_enable