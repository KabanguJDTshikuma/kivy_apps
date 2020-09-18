from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App

class Lean_widgetApp(BoxLayout):
    pass


class widgetApp(App):
    def build(self):
        return Lean_widgetApp()

if __name__=="__main__":
    widgetApp().run()