from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout


class Menu(Screen):
    pass


class ReviewMenu(Screen):
    pass


class Transition(ScreenManager):
    pass


class CreateFlashcard(Screen):

    word = ObjectProperty(None)
    meaning = ObjectProperty(None)

    word_list = ObjectProperty([])
    meaning_list = ObjectProperty([])

    def add(self):
        if self.word.text == "" or self.meaning.text == "":
            self.show_popup()

        else:
            self.word_list.append(self.word.text)
            self.meaning_list.append(self.meaning.text)
            self.word.text = ""
            self.meaning.text = ""

    def remove(self):
        if not self.word_list:
            self.word.text = ""
            self.meaning.text = ""
        else:
            self.word_list.remove(self.word_list[-1])
            self.meaning_list.remove(self.meaning_list[-1])
            print(self.word_list, self.meaning_list)
            self.word.text = ""
            self.meaning.text = ""

    @staticmethod
    def show_popup():
        popupWindow = GridLayout(cols=1, padding=10)
        popup_content = Label(text="Oops! Please enter the required information ")
        popup_btn = Button(text="Got it!", size_hint=(None, None),
                           width=360, height=54)

        popupWindow.add_widget(popup_content)
        popupWindow.add_widget(popup_btn)

        popup_win = Popup(title='Error!', content=popupWindow,
                          size_hint=(None, None), size=(400, 300))
        popup_win.open()
        popup_btn.bind(on_press=popup_win.dismiss)

    def words(self):
        return self.word_list

    def meanings(self):
        return self.meaning_list

    pass


class PopWin(FloatLayout):
    pass
