from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App

class Lean_floatLayoutApp(FloatLayout):
    pass


class floatlayApp(App):
    def build(self):
        return Lean_floatLayoutApp()

if __name__=="__main__":
    floatlayApp().run()