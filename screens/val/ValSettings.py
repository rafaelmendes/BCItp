from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from utils import saveObjAsJson

from standards import *

class ValSettings(Screen):
# layout
    def __init__ (self, session_header,**kwargs):
        super (ValSettings, self).__init__(**kwargs)
        self.sh = session_header

        boxg = BoxLayout(padding=10, spacing=10, orientation='vertical')

        box_bottom = BoxLayout(size_hint_x=1, size_hint_y=0.3,padding=10, spacing=10, orientation='vertical')

        self.label_msg = Label(text="", font_size=FONT_SIZE)
        
        button_save = Button(text="Save", size = BUTTON_SIZE)
        button_save.bind(on_press= self.save_config)

        button_back = Button(text="Back", size = BUTTON_SIZE)
        button_back.bind(on_press= self.change_to_cal)

        box_top = BoxLayout(size_hint_x=1, size_hint_y=0.3,padding=10, spacing=10, orientation='vertical')

        self.n_trials = TextInput(size_hint=(1, 0.8), font_size= FONT_SIZE,
                        hint_text='Number of Trials', multiline=False)

        self.pause_offset = TextInput(size_hint=(1, 0.8), font_size= FONT_SIZE,
                        hint_text='Pause Offset', multiline=False)

        self.cue_offset = TextInput(size_hint=(1, 0.8), font_size= FONT_SIZE,
                        hint_text='Cue Offset', multiline=False)

        self.end_trial_offset = TextInput(size_hint=(1, 0.8), font_size= FONT_SIZE,
                        hint_text='End of Trial Offset', multiline=False)


        box_top.add_widget(self.n_trials)
        box_top.add_widget(self.pause_offset)
        box_top.add_widget(self.cue_offset)
        box_top.add_widget(self.end_trial_offset)

        box_bottom.add_widget(self.label_msg)
        box_bottom.add_widget(button_save)
        box_bottom.add_widget(button_back)

        boxg.add_widget(box_top)
        boxg.add_widget(box_bottom)

        self.add_widget(boxg)


    def change_to_cal(self,*args):
        self.manager.current = 'ValMenu'
        self.manager.transition.direction = 'right'

    def save_config(self,*args):

        self.sh.v_n_trials = self.n_trials.text
        self.sh.v_cue_offset =  self.cue_offset.text
        self.sh.v_pause_offset =  self.pause_offset.text
        self.sh.v_end_trial_offset =  self.end_trial_offset.text

        self.sh.data_val_path = PATH_TO_SESSION + self.sh.name + '/' + 'data_val.txt'
        self.sh.events_val_path = PATH_TO_SESSION + self.sh.name + '/' + 'events_val.txt'
    
        saveObjAsJson(self.sh, PATH_TO_SESSION + self.sh.name + '/' + 'session_info.txt')
        self.label_msg.text = "Settings Saved!"