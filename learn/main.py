from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)

from kivy.graphics.context_instructions import Color

import random


class ScatterTextWidget(BoxLayout):

    text_colour = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__()

        # with self.canvas.before:
        #     Color(0, 1, 0, 1)
        #     Rectangle(pos=(0, 100), size=(300, 100))
        #     Ellipse(pos=(0, 400), size=(300, 100))
        #     Line(points=[0, 0, 500, 600, 400, 300],
        #          close=True,
        #          width=3)

    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        self.text_colour = colour


        label1 = self.ids.label1
        label2 = self.ids.label2

        label1.color = colour
        label2.color = colour


class MyApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    MyApp().run()

