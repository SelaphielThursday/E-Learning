from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from Flashcard import CreateFlashcard


class Slideshow(Screen):
    word_slide = StringProperty("Word")
    meaning_slide = StringProperty("Meaning")

    place = 0

    def start(self):

        self.word_slide = (CreateFlashcard().words()[self.place])
        self.meaning_slide = (CreateFlashcard().meanings()[self.place])
        return self.place, self.word_slide, self.meaning_slide

    def prev(self):

        self.place = self.place - 1
        if self.place < 0:
            self.place = len(CreateFlashcard().words()) - 1
            self.word_slide = CreateFlashcard().words()[self.place]
            self.meaning_slide = CreateFlashcard().meanings()[self.place]
            return self.place, self.word_slide, self.meaning_slide
        else:
            self.word_slide = CreateFlashcard().words()[self.place]
            self.meaning_slide = CreateFlashcard().meanings()[self.place]
            return self.place, self.word_slide, self.meaning_slide

    def next(self):
        self.place = self.place + 1
        maximum = len(CreateFlashcard().words())
        if self.place >= maximum:
            self.place = 0
            self.word_slide = CreateFlashcard().words()[self.place]
            self.meaning_slide = CreateFlashcard().meanings()[self.place]
            return self.place, self.word_slide, self.meaning_slide

        else:
            self.word_slide = CreateFlashcard().words()[self.place]
            self.meaning_slide = CreateFlashcard().meanings()[self.place]
            return self.place, self.word_slide, self.meaning_slide

    pass
