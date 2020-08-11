import random
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from Flashcard import CreateFlashcard


class Quiz(Screen):
    choices = 0
    shuffle_word = StringProperty("WORD")
    shuffle_meaning = StringProperty("MEANING")
    digit = 0

    def quiz_word(self):
        self.choices = list(range(len(CreateFlashcard().words())))
        random.shuffle(self.choices)
        self.shuffle_word = CreateFlashcard().words()[self.choices[self.digit]]
        return self.choices, self.shuffle_word

    def show(self):
        self.shuffle_meaning = CreateFlashcard().meanings()[self.choices[self.digit]]
        return self.digit, self.shuffle_meaning

    def next_word(self):
        self.digit = self.digit + 1
        maximum = len(CreateFlashcard().words())
        self.shuffle_meaning = ""
        if self.digit >= maximum:
            self.digit = 0
            self.shuffle_word = CreateFlashcard().words()[self.choices[self.digit]]
            return self.digit, self.shuffle_word
        else:
            self.shuffle_word = CreateFlashcard().words()[self.choices[self.digit]]
            return self.digit, self.shuffle_word

    pass
