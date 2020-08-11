import kivy
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from random import shuffle
from Flashcard import CreateFlashcard
from slideshow import Slideshow
from quiz import Quiz

LabelBase.register(name="Carrington", fn_regular="Carrington.ttf")
LabelBase.register(name="SciFly", fn_regular="SciFly-Sans.ttf")
LabelBase.register(name="Origicide", fn_regular="Origicide.ttf")


Window.clearcolor = (12/255.0, 39/255.0, 26/255.0, 0)


class FontApp(App):
    pass


class Menu(Screen):
    pass


class ReviewMenu(Screen):
    pass


class Transition(ScreenManager):
    pass


kv = Builder.load_file("flashcard.kv")


class Flashcard(App):
    def build(self):
        return kv


if __name__ == "__main__":
    Flashcard().run()
